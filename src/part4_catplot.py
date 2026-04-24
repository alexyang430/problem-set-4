'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt


def catplot_felony_prediction(pred_universe):
    '''
    1. Creates a catplot where categories are charge type (has_felony_charge)
       and the y-axis is the prediction for felony rearrest. kind='bar'.

    Parameters:
    - pred_universe dataframe (merged with felony_charge)

    Returns:
    - Catplot saved to data/part4_plots/catplot_felony_prediction.png
    '''
    g = sns.catplot(data=pred_universe, x='has_felony_charge', y='prediction_felony', hue='has_felony_charge', kind='bar', palette='Set2', legend=False)
    g.set_axis_labels('Has Felony Charge', 'Predicted Probability of Felony Rearrest')
    g.figure.suptitle('Felony Rearrest Prediction by Current Charge Type', y=1.02)
    plt.savefig('./data/part4_plots/catplot_felony_prediction.png', bbox_inches='tight')
    plt.close()


def catplot_nonfelony_prediction(pred_universe):
    '''
    2. Creates a catplot where categories are charge type (has_felony_charge)
       and the y-axis is the prediction for nonfelony rearrest. kind='bar'.

    Parameters:
    - pred_universe dataframe (merged with felony_charge)

    Returns:
    - Catplot saved to data/part4_plots/catplot_nonfelony_prediction.png
    '''
    g = sns.catplot(data=pred_universe, x='has_felony_charge', y='prediction_nonfelony', hue='has_felony_charge', kind='bar', palette='Set2', legend=False)
    g.set_axis_labels('Has Felony Charge', 'Predicted Probability of Nonfelony Rearrest')
    g.figure.suptitle('Nonfelony Rearrest Prediction by Current Charge Type', y=1.02)
    plt.savefig('./data/part4_plots/catplot_nonfelony_prediction.png', bbox_inches='tight')
    plt.close()

    print(
        "What might explain the difference between the plots?\n"
        "Arrestees with a current felony charge have a higher predicted probability of felony rearrest "
        "than those with only misdemeanor charges, which is expected — current charge severity is a strong "
        "predictor of future charge severity. However, the nonfelony rearrest predictions show less separation "
        "between the two groups (or even higher nonfelony predictions for misdemeanor-only arrestees). "
        "This may be because misdemeanor offenders tend to be arrested more frequently for lower-level crimes, "
        "driving up their nonfelony rearrest risk scores, while felony offenders are flagged primarily for "
        "felony recidivism risk. The model likely weights different features for each outcome."
    )


def catplot_felony_prediction_hued(pred_universe):
    '''
    3. Repeats plot from (1) but hues by whether the person was actually rearrested
       for a felony crime (recidivism_felony).

    Parameters:
    - pred_universe dataframe (merged with felony_charge)

    Returns:
    - Catplot saved to data/part4_plots/catplot_felony_prediction_hued.png
    '''
    g = sns.catplot(data=pred_universe, x='has_felony_charge', y='prediction_felony', hue='y_felony', kind='bar', palette='Set1')
    g.set_axis_labels('Has Felony Charge', 'Predicted Probability of Felony Rearrest')
    g.figure.suptitle('Felony Rearrest Prediction by Charge Type and Actual Recidivism', y=1.02)
    plt.savefig('./data/part4_plots/catplot_felony_prediction_hued.png', bbox_inches='tight')
    plt.close()

    print(
        "What does it mean that prediction for arrestees with a current felony charge, "
        "but who did not get rearrested for a felony crime have a higher predicted probability than "
        "arrestees with a current misdemeanor charge, but who did get rearrested for a felony crime?\n"
        "It means the model is making errors in both directions. For felony-charge arrestees who did NOT "
        "reoffend, the model over-predicted their risk — assigning them a high probability of felony rearrest "
        "that did not materialize (false positives). For misdemeanor-charge arrestees who DID reoffend with a "
        "felony, the model under-predicted their risk — assigning them a lower probability even though they "
        "went on to commit a felony (false negatives). This suggests the model relies heavily on current charge "
        "type as a feature, potentially at the expense of other factors that better predict actual recidivism. "
        "It also highlights a fairness concern: people may be over-penalized based on charge type alone, "
        "independent of their actual future behavior."
    )
