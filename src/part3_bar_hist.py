'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt


def fta_barplot(pred_universe):
    '''
    1. Creates a bar plot for the fta column from pred_universe.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Bar plot of fta counts saved to data/part3_plots/fta_barplot.png
    '''
    fta_counts = pred_universe.groupby('fta').size().reset_index(name='count')

    plt.figure()
    sns.barplot(data=fta_counts,x='fta',y='count',color='steelblue')
    plt.title('Failure to Appear (FTA) Counts')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')
    plt.close()


def fta_barplot_by_sex(pred_universe):
    '''
    2. Creates a bar plot for the fta column from pred_universe, hued by sex.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Bar plot of fta counts hued by sex saved to data/part3_plots/fta_barplot_by_sex.png
    '''
    fta_sex_counts = pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count')

    plt.figure()
    sns.barplot(data=fta_sex_counts,x='fta',y='count',hue='sex')
    plt.title('Failure to Appear (FTA) Counts by Sex')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.legend(title='Sex')
    plt.savefig('./data/part3_plots/fta_barplot_by_sex.png', bbox_inches='tight')
    plt.close()


def age_histogram(pred_universe):
    '''
    3. Plots a histogram of age_at_arrest.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram of age_at_arrest saved to data/part3_plots/age_histogram.png
    '''
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest', color='steelblue')
    plt.title('Distribution of Age at Arrest')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Count')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')
    plt.close()


def age_histogram_binned(pred_universe):
    '''
    4. Plots a histogram of age_at_arrest with bins representing age groups:
       18-21, 21-30, 30-40, 40-100.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Binned histogram of age_at_arrest saved to data/part3_plots/age_histogram_binned.png
    '''
    plt.figure()
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=[18, 21, 30, 40, 100], color='steelblue')
    plt.title('Age at Arrest by Age Group')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Count')
    plt.xticks([18, 21, 30, 40, 100])
    plt.savefig('./data/part3_plots/age_histogram_binned.png', bbox_inches='tight')
    plt.close()
