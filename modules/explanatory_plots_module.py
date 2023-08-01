import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plots_module as plt_mod

def Init(df):
    global df_transactions_clean
    df_transactions_clean = df

def ExpVisualization1():
    category_fraud_count = df_transactions_clean.groupby('category')['is_fraud'].sum().sort_values(ascending=False)
    category_labels = category_fraud_count.index
    
    plot_title = 'Count Of Fraud Transactions Per Category'
    plot_labels = ['Fraud Transactions Count', 'Category']
    sb.barplot(x=category_fraud_count, y=category_labels, color=plt_mod.default_plot_color)
    plt_mod.InitAxesLabels(plot_title, plot_labels)
    
def ExpVisualization2():
    top_15_zip_codes = df_transactions_clean['zip'].value_counts(ascending=False)[:15]
    zip_codes_labels = top_15_zip_codes.index.astype(str)
    
    zip_codes_fraud_grouped = df_transactions_clean.groupby('zip')['is_fraud'].sum().sort_values(ascending=False)[:15]
    zip_codes_fraud_values = zip_codes_fraud_grouped.values
    zip_codes_fraud_labels = zip_codes_fraud_grouped.index.astype(str)
    
    plot_title = 'Top 15 ZIP Codes With Highest Fraud Transactions'
    plot_labels = ['Fraud Count', 'ZIP Codes']
    plt_mod.SetupCompareBarPlot(zip_codes_fraud_values, zip_codes_fraud_labels, zip_codes_labels, ['Not in Top 15 ZIP Codes', 'In Top 15 ZIP Codes'])
    plt_mod.InitAxesLabels(plot_title, plot_labels)
    
def ExpVisualization3():
    top_15_jobs = df_transactions_clean['job'].value_counts(ascending=False)[:15]
    top_15_jobs_labels = top_15_jobs.index
    
    top_job_fraud = df_transactions_clean.groupby('job')['is_fraud'].sum().sort_values(ascending=False)[:15]
    top_job_fraud_labels = top_job_fraud.index
    top_job_fraud_values = top_job_fraud.values
    
    plot_title = 'Top Jobs With The Highest Frauds Count'
    plot_labels = ['Fraud Count', 'Job Title']
    plt_mod.SetupCompareBarPlot(top_job_fraud_values, top_job_fraud_labels, top_15_jobs_labels, ['Not In Top 15 Jobs', 'In Top 15 Jobs'])
    plt_mod.InitAxesLabels(plot_title, plot_labels)
    
def ExpVisualization4():
    top_cities = df_transactions_clean['city'].value_counts(ascending=False)[:15]
    top_states = df_transactions_clean['state'].value_counts(ascending=False)[:15]
    top_cities_labels = top_cities.index
    top_states_labels = top_states.index
    
    top_cities_fraud = df_transactions_clean.groupby('city')['is_fraud'].sum().sort_values(ascending=False)[:15]
    top_states_fraud = df_transactions_clean.groupby('state')['is_fraud'].sum().sort_values(ascending=False)[:15]
    top_cities_fraud_labels = top_cities_fraud.index
    top_cities_fraud_values = top_cities_fraud.values
    top_states_fraud_labels = top_states_fraud.index
    top_states_fraud_values = top_states_fraud.values
    
    cities_bar_colors = [plt_mod.default_plot_color] * top_cities_fraud_values.size
    states_bar_colors = [plt_mod.default_plot_color] * top_states_fraud_values.size

    cities_labels_in_top15 = top_cities_fraud_labels.isin(top_cities_labels)
    states_labels_in_top15 = top_states_fraud_labels.isin(top_states_labels)
    city_plot_hatch = ['' for _ in range(top_cities_fraud_values.size)]
    state_plot_hatch = ['' for _ in range(top_states_fraud_values.size)]

    for i in range(cities_labels_in_top15.size):
        if cities_labels_in_top15[i] == True:
            city_plot_hatch[i] = 'ooo'
            cities_bar_colors[i] = plt_mod.orange_plot_color
        
    for i in range(states_labels_in_top15.size):
        if states_labels_in_top15[i] == True:
            state_plot_hatch[i] = 'ooo'
            states_bar_colors[i] = plt_mod.orange_plot_color
            
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Top 15 City And State With The Highest Fraud Transactions Count')
    fig.supxlabel('Frauds Count')
    sb.barplot(ax=ax[0], x=top_cities_fraud_values, y=top_cities_fraud_labels, palette=cities_bar_colors, hatch=city_plot_hatch, edgecolor='black')
    sb.barplot(ax=ax[1], x=top_states_fraud_values, y=top_states_fraud_labels, palette=states_bar_colors, hatch=state_plot_hatch, edgecolor='black')

    hatched_patch = mpatches.Patch(facecolor=plt_mod.orange_plot_color, edgecolor='black', hatch='ooo', label='In Top 15 Cities/States Plot')
    regular_patch = mpatches.Patch(facecolor=plt_mod.default_plot_color, edgecolor=plt_mod.default_plot_color, label='Not In Top 15 Cities/States Plot')
    plt.legend(handles=[hatched_patch, regular_patch], bbox_to_anchor=(1, 1));
    
def ExpVisualization5():
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fraud_transactions = df_transactions_clean[df_transactions_clean['is_fraud']]
    month_fraud_transactions = fraud_transactions.groupby(fraud_transactions['trans_datetime'].dt.month).size()
    day_fraud_transactions = fraud_transactions.groupby(fraud_transactions['trans_datetime'].dt.day).size()
    month_fraud_transactions_values = month_fraud_transactions.values
    day_fraud_transactions_labels = day_fraud_transactions.index.astype(str)
    day_fraud_transactions_values = day_fraud_transactions.values
    
    month_bar_colors = [plt_mod.default_plot_color] * month_fraud_transactions_values.size
    day_bar_colors = [plt_mod.default_plot_color] * day_fraud_transactions_values.size

    month_fraud_plot_hatch = ['' for _ in range(month_fraud_transactions_values.size)]
    day_fraud_plot_hatch = ['' for _ in range(day_fraud_transactions_values.size)]

    month_fraud_plot_hatch[month_fraud_transactions_values.argmax()] = '///'
    day_fraud_plot_hatch[day_fraud_transactions_values.argmax()] = '///'
    month_bar_colors[month_fraud_transactions_values.argmax()] = plt_mod.orange_plot_color
    day_bar_colors[day_fraud_transactions_values.argmax()] = plt_mod.orange_plot_color

    month_fraud_plot_hatch[month_fraud_transactions_values.argmin()] = 'ooo'
    day_fraud_plot_hatch[day_fraud_transactions_values.argmin()] = 'ooo'
    month_bar_colors[month_fraud_transactions_values.argmin()] = plt_mod.orange_plot_color
    day_bar_colors[day_fraud_transactions_values.argmin()] = plt_mod.orange_plot_color
    
    fig, ax = plt.subplots(1, 2, figsize=(17, 8))
    fig.suptitle('Count Of Fraud Transactions For Each Month And Day')
    fig.supxlabel('Fraud Count')
    sb.barplot(ax=ax[0], x=month_fraud_transactions_values, y=month_labels, palette=month_bar_colors, hatch=month_fraud_plot_hatch, edgecolor='black')
    ax[0].set_ylabel('Month')
    sb.barplot(ax=ax[1], x=day_fraud_transactions_values, y=day_fraud_transactions_labels, palette=day_bar_colors, hatch=day_fraud_plot_hatch, edgecolor='black');
    ax[1].set_ylabel('Day')

    highest_patch = mpatches.Patch(facecolor=plt_mod.orange_plot_color, edgecolor='black', hatch='///', label='Highest Value')
    lowest_patch = mpatches.Patch(facecolor=plt_mod.orange_plot_color, edgecolor='black', hatch='oo', label='Lowest Value')
    regular_patch = mpatches.Patch(facecolor=plt_mod.default_plot_color, edgecolor=plt_mod.default_plot_color, label='Regular Value')
    plt.legend(handles=[highest_patch, lowest_patch, regular_patch], bbox_to_anchor=(1, 1));
    
def ExpVisualization6():
    xticks = [1, 10, 100, 1000, 2000]
    yticks = [[0, 0.2, 0.4, 0.6, 0.8, 1], ['0%', '20%', '40%', '60%', '80%', '100%']]
    fraud_frequency = df_transactions_clean.groupby('amt')['is_fraud'].mean()
    fig, ax1 = plt.subplots(figsize=(10, 6))
    sb.regplot(ax=ax1, x=fraud_frequency.index, y=fraud_frequency.values, scatter_kws={'alpha': 0.4}, x_jitter=0.2, y_jitter=0.1, color=plt_mod.orange_plot_color, fit_reg=False)
    ax1.set_xlabel('Transaction Cost (log scale)')
    ax1.set_ylabel('Precentage Of Fraud Transactions')
    ax1.set_yticks(yticks[0], yticks[1])
    ax1.set_ylim(0, 1)
    ax2 = ax1.twinx()
    sb.histplot(ax=ax2, data=df_transactions_clean, x='amt', color=plt_mod.default_plot_color)
    plt.xscale('log')
    plt.xlim(1, 2000);
    plt.title('Distribution Of Transactions Cost Against Fraud Transactions')
    plt.xticks(xticks, xticks)
    plt.legend(handles=[ax1.collections[0], ax2.patches[0]], labels=['Fraud Transactions', 'Normal Transactions'], loc='upper left', bbox_to_anchor=(1.1, 1));
    
def ExpVisualization7():
    xticks = [1, 10, 100, 1000, 10000]
    fraud_transactions = df_transactions_clean[df_transactions_clean['is_fraud']]
    plot_title = 'Difference Betweeen Fraud And Normal Transactions For Each Category'
    plot_labels = ['Transaction Cost (log scale)', 'Category']
    sb.regplot(data=df_transactions_clean, x='amt', y='category', scatter_kws={'alpha': 0.2}, fit_reg=False, color=plt_mod.default_plot_color, label='Normal Transactions')
    sb.regplot(data=fraud_transactions, x='amt', y='category', scatter_kws={'alpha': 0.4}, fit_reg=False, color=plt_mod.orange_plot_color, marker='D', label='Fraud Transactions')
    plt.xscale('log')
    plt.xlim(1, 10000)
    plt.xticks(xticks, xticks)
    plt_mod.InitAxesLabels(plot_title, plot_labels)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1));