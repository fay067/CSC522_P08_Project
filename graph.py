from rfm import *
from data import *
from tf_idf import *
from kmeans import *
import matplotlib.pyplot as plt

'''
Author: Chu-Wen Chen
Credit for Radar Chart: Fabien Daniel
'''


# df should be the result of customer clustering without normalization
def df_for_chart(df, n_product_cate):
    ori_customer_rfm = df.drop(columns=["Recency"]).copy()
    ori_customer_rfm["Amount per Visit"] = df['Amount'] / df['Frequency']
    # Group by cluster label
    customer_cluster = pd.DataFrame()
    customer_cluster['Cluster'] = ori_customer_rfm['Cluster'].unique()
    customer_cluster['Sum $'] = customer_cluster["Cluster"].map(
        ori_customer_rfm.groupby("Cluster")["Amount"].sum().to_dict().get)
    customer_cluster['Med. $'] = customer_cluster["Cluster"].map(
        ori_customer_rfm.groupby("Cluster")["Amount"].median().to_dict().get)
    customer_cluster['Size'] = customer_cluster["Cluster"].map(
        ori_customer_rfm.groupby("Cluster")["CustomerID"].nunique().to_dict().get)
    customer_cluster['Med. Visit'] = customer_cluster["Cluster"].map(
        ori_customer_rfm.groupby("Cluster")["Frequency"].median().to_dict().get)
    customer_cluster['Median $ per Visit'] = customer_cluster["Cluster"].map(
       ori_customer_rfm.groupby("Cluster")["Amount per Visit"].median().to_dict().get)
    for i in range(1, n_product_cate+1):
        col1 = 'cate_{}'.format(i)
        customer_cluster[col1] = customer_cluster["Cluster"].map(
            ori_customer_rfm.groupby("Cluster")[col1].sum().to_dict().get) / customer_cluster['Sum $'] * 100
        col2 = '{} mean'.format(col1)
        customer_cluster[col2] = customer_cluster["Cluster"].map(
            ori_customer_rfm.groupby("Cluster")[col1].mean().to_dict().get)
        col3 = '{} std'.format(col1)
        customer_cluster[col3] = customer_cluster["Cluster"].map(
            ori_customer_rfm.groupby("Cluster")[col1].std(ddof=0).to_dict().get)
    customer_cluster.set_index('Cluster', inplace=True)
    return customer_cluster


# Create Radar Chart for each customer cluster
def _scale_data(data, ranges):
    (x1, x2) = ranges[0]
    d = data[0]
    return [(d - y1) / (y2 - y1) * (x2 - x1) + x1 for d, (y1, y2) in zip(data, ranges)]


class RadarChart:
    def __init__(self, fig, location, sizes, variables, ranges, n_ordinate_levels=6):
        angles = np.arange(0, 360, 360. / len(variables))
        ix, iy = location[:]
        size_x, size_y = sizes[:]
        axes = [fig.add_axes([ix, iy, size_x, size_y], polar=True,
                             label="axes{}".format(i)) for i in range(len(variables))]
        _, text = axes[0].set_thetagrids(angles, labels=variables)
        for txt, angle in zip(text, angles):
            if angle > -1 and angle < 181:
                txt.set_rotation(angle - 90)
            else:
                txt.set_rotation(angle - 270)
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.xaxis.set_visible(False)
            ax.grid(False)
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i], num=n_ordinate_levels)
            grid_label = [""] + ["{:.0f}".format(x) for x in grid[1:-1]]
            ax.set_rgrids(grid, labels=grid_label, angle=angles[i])
            ax.set_ylim(*ranges[i])
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]

    def plot(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def fill(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def legend(self, *args, **kw):
        self.ax.legend(*args, **kw)

    def title(self, title, *args, **kw):
        self.ax.text(0.9, 1, title, transform=self.ax.transAxes, *args, **kw)


# In our case, df should be something returned from function "df_for_chart"
def radar_chart(df, n_clusters, n_attributes):
    fig = plt.figure(figsize=(10, 12))
    attributes = []
    for i in range(1, n_attributes+1):
        col = 'cate_{}'.format(i)
        attributes.append(col)
    ranges = [[0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30],
              [0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30], [0.01, 30]]
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n_groups = n_clusters
    i_cols = 3
    i_rows = n_groups // i_cols
    size_x, size_y = (1 / i_cols), (1 / i_rows)

    for ind in range(n_clusters):
        ix = ind % 3
        iy = i_rows - ind // 3
        pos_x = ix * (size_x + 0.05)
        pos_y = iy * (size_y + 0.05)
        location = [pos_x, pos_y]
        sizes = [size_x, size_y]
        data = np.array(df.loc[index[ind], attributes])
        radar = RadarChart(fig, location, sizes, attributes, ranges)
        radar.plot(data, color='b', linewidth=2.0)
        radar.fill(data, alpha=0.2, color='b')
        radar.title(title='cluster {}'.format(index[ind]), color='r')
        ind += 1


# In our case, df should be the result of customer clustering without normalization
def pie_chart(df, cluster_n, attribute_n):
    # Purchases division
    col = 'cate_{}'.format(attribute_n)
    amount_max = df[df["Cluster"] == cluster_n][col].max()
    amount_min = df[df["Cluster"] == cluster_n][col].min()
    unit = (amount_max - amount_min) / 28
    current_threshold = 0.0
    # price_range = [0, 50, 100, 200, 500, 1000, 5000, 50000]
    price_range = []
    for i in range(8):
        price_range.append(current_threshold)
        current_threshold = current_threshold + i * unit
    count_price = []
    basket_price = df[df['Cluster'] == cluster_n].copy()
    # display(basket_price.head(5))
    for i, price in enumerate(price_range):
        if i == 0: continue
        val = basket_price[(basket_price[col] < price) &
                           (basket_price[col] > price_range[i - 1])][col].count()
        count_price.append(val)
    # visualize the purchase division for a customer cluster to a product category
    plt.rc('font', weight='bold')
    f, ax = plt.subplots(figsize=(11, 6))
    colors = ['yellowgreen', 'gold', 'wheat', 'c', 'violet', 'royalblue', 'firebrick']
    labels = ['{:.2f}<.<{:.2f}'.format(price_range[i - 1], s) for i, s in enumerate(price_range) if i != 0]
    sizes = count_price
    explode = [0.0 if sizes[i] < 100 else 0.0 for i in range(len(sizes))]
    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct=lambda x: '{:1.0f}%'.format(x) if x > 1 else '',
           shadow=False, startangle=0)
    ax.axis('equal')
    f.text(0.5, 1.01, "Customer Cluster 1 Purchase amount division on product category 2", ha='center', fontsize=18)


if __name__ == "__main__":
    df = load_data()
    matrix = tf_idf(df)
    sse, sscore, test_range = kmeans(matrix)
    clusters = kmeans(matrix=matrix, cluster_num=6, score=sscore[6])
    df = tf_idf_write_back(df, clusters)
    tf_idf_rfm = rfm(df, 1)
    matrix = rfm_matrix(tf_idf_rfm)
    sse, sscore, test_range = kmeans(matrix)
    clusters = kmeans(matrix=matrix, cluster_num=5, score=sscore[5])
    tf_idf_rfm = rfm_write_back(tf_idf_rfm, clusters)
    tf_idf_rfm.rename(columns={'Group': 'Cluster'}, inplace=True)
    n_attributes = len(tf_idf_rfm.columns) - 5
    customer_clustering = df_for_chart(tf_idf_rfm, n_attributes)
    n_clusters = len(customer_clustering.index)
    radar_chart(customer_clustering, n_clusters, n_attributes)
    pie_chart(tf_idf_rfm, 1, 2)


