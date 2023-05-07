# Tria-nauts Stroke Risk Calculator

Welcome to Team Tria-nauts' Stroke Risk Calculator! Our team has built this tool to predict a user's risk of developing stroke disease based on the likelihood that someone similar to you has had a stroke. Our Machine Learning model was trained using approximately 430,000 survey responses from U.S. Residents collected by The CDC BRFSS data. This calculator utilizes carefully picked out parameters ranging from factors such as BMI to smoking status, and aims to produce a binary response as to whether an individual is at risk for a stroke, with an accuracy of approximately 93%. 

## Requirements

This project uses poetry to maintain its dependencies. To install run

```bash
poetry install

```

## Usage

To run the stroke calculator use the following command

```bash
poetry run python3 src/dash/app.py
```

All models and data transformations are contained in the src/notebooks folder. To run everything in order use the command

```bash
./run_all.sh
```

## Examples

To use the calculator, you are required to enter some information about your health conditions/measures. Then, select "Calculate" at the bottom to run our model and be produced with a binary yes or no response. Select "Reset" to reset the calculator inputs. Refer to the gif below: 

![](BorealisAI.gif)


## Disclaimers

DISCLAIMER: The following calculator was produced as a part of RBC Borealis AI's Let's SOLVE It Program, by a team of three first-year computer science students from the University of Waterloo; Chiara Alcantara, Franklin Ramirez, and Helena Xu. This is NOT a substitute for a medically-accurate stroke risk calculator. Please reach out to your family doctor/nearest health facility if you believe to be at risk of a stroke/need immediate medical attention. Alternatively, feel free to check out the following stroke risk calculators: https://clincalc.com/Cardiology/ASCVD/PooledCohort.aspx
https://www.projectbiglife.ca/cardiovascular-disease

## License

CC BY-NC 2.0
