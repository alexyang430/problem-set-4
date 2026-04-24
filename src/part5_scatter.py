'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt


def scatter_felony_nonfelony_by_charge(pred_universe):
    '''
    1. Creates a scatter plot (lmplot) with x=prediction_felony, y=prediction_nonfelony,
       hued by whether the current charge is a felony (has_felony_charge).

    Parameters:
    - pred_universe dataframe (merged with felony_charge)

    Returns:
    - Scatterplot saved to data/part5_plots/scatter_by_charge_type.png
    '''
    sp = sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony', hue='has_felony_charge', fit_reg=False, palette='Set1', scatter_kws={'alpha': 0.4, 's': 15})
    sp.set_axis_labels('Predicted Probability of Felony Rearrest', 'Predicted Probability of Nonfelony Rearrest')
    sp.figure.suptitle('Felony vs. Nonfelony Rearrest Predictions by Current Charge Type', y=1.02)
    plt.savefig('./data/part5_plots/scatter_by_charge_type.png', bbox_inches='tight')
    plt.close()

    print(
        "What can you say about the group of dots on the right side of the plot?\n"
        "The group of dots on the right side of the plot — those with high predicted felony rearrest "
        "probabilities — are predominantly arrestees with a current felony charge (has_felony_charge=True). "
        "This cluster suggests that the model assigns high felony recidivism risk largely to those already "
        "charged with a felony. These individuals also tend to have relatively high nonfelony predictions, "
        "indicating the model sees them as generally high-risk across both outcome types. The separation "
        "between the two hue groups is most pronounced at higher felony prediction values, reinforcing that "
        "current felony charge is a dominant driver of the model's felony rearrest score."
    )


def scatter_felony_prediction_vs_recidivism(pred_universe):
    '''
    2. Creates a scatter plot with x=prediction_felony, y=recidivism_felony
       (whether someone was actually rearrested for a felony).

    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatterplot saved to data/part5_plots/scatter_prediction_vs_recidivism.png
    '''
    sp = sns.lmplot(data=pred_universe, x='prediction_felony', y='y_felony', fit_reg=True, scatter_kws={'alpha': 0.2, 's': 10}, line_kws={'color': 'red'})
    sp.set_axis_labels('Predicted Probability of Felony Rearrest', 'Actually Rearrested for Felony (0/1)')
    sp.figure.suptitle('Model Calibration: Felony Rearrest Prediction vs. Actual Outcome', y=1.02)
    plt.savefig('./data/part5_plots/scatter_prediction_vs_recidivism.png', bbox_inches='tight')
    plt.close()

    print(
        "Would you say based off of this plot if the model is calibrated or not?\n"
        "A perfectly calibrated model would show a regression line close to the diagonal — meaning that "
        "when the model predicts a 0.3 probability, about 30% of those people actually reoffended, and so on. "
        "If the regression line is relatively flat or does not track closely with actual outcomes across the "
        "probability range, the model is poorly calibrated. Given that the outcome variable is binary (0/1), "
        "we'd expect a well-calibrated model to show a positive, roughly linear trend between predicted "
        "probability and actual recidivism rate. If the slope is shallow or the predicted probabilities cluster "
        "in a narrow range regardless of actual outcome, the model is not well-calibrated — it may be assigning "
        "similar scores to people with very different actual outcomes, limiting its usefulness for decision-making."
    )
