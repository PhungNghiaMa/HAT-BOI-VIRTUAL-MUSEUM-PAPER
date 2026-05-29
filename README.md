# HAT-BOI-VIRTUAL-MUSEUM-PAPER GUIDANCE

## How to run the code 
1. Clone the repository to your local machine using:
   ```
   git clone
    ```
2. Navigate to the project directory:
   ```
    cd HAT-BOI-VIRTUAL-MUSEUM-PAPER/PAPER/.venv
    ```
3. Install all required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

4. Run the main script:
    ```
    python analyze.py
    ```

## Project Overview
This repository contains the data and analytical scripts for the user study evaluating the Virtual Art Museum for Hat Boi (Vietnamese classical opera) against a standard Baseline (e.g., Artsteps , Google Art & Culture).

The study used a within-subjects, counterbalanced design ($N=36$) to measure the difference in perceived Usability and User Experience between the two systems. The analysis conclusively demonstrates the superior quality of the immersive Virtual Museum platform across all measured metrics.

### Survey Instruments Used in the User Study


This section details the standardized questionnaires used to evaluate the user experience of the Virtual Art Museum (Museum) and the Control (Baseline) conditions.

### A. System Usability Scale (SUS)

The SUS is a 10-item questionnaire scored on a 5-point scale, where 1 = Strongly Disagree and 5 = Strongly Agree. Even-numbered items are negatively worded and reverse-scored.

 1. I think that I would like to use this system frequently.

 2. I found the system unnecessarily complex. (Reverse-scored)

 3. I thought the system was easy to use.

 4. I think that I would need the support of a technical person to be able to use the system. (Reverse-scored)
 
 5. I found the various functions in this system were well integrated.

 6. I thought there was too much inconsistency in the system. (Reverse-scored)

 7. I would imagine that most people would learn to use this system very quickly.

 8. I found the system very cumbersome to use. (Reverse-scored)

 9. I felt very confident using the system.
 
 10. I needed to learn a lot of things before I could get going with the system. (Reverse-scored)
 
 ## B. User Experience Questionnaire - Short (UEQ-S)
 
 The UEQ-S is an 8-item questionnaire measuring Pragmatic and Hedonic Quality on a 7-point semantic differential scale. The scoring ranges from 1 (Negative Pole) to 7 (Positive Pole).

| Item | Negative Pole (1) | Positive Pole (7) | Quality Dimension | 
| ----- | ----- | ----- | ----- | 
| **P1** | Annoying | Enjoyable | Pragmatic | 
| **P2** | Not easy to use | Easy to use | Pragmatic | 
| **P3** | Not effective | Effective | Pragmatic | 
| **P4** | Impeding | Supporting | Pragmatic | 
| **H1** | Boring | Exciting | Hedonic | 
| **H2** | Not interesting | Interesting | Hedonic | 
| **H3** | Usual | Inventive | Hedonic | 
| **H4** | Conventional | Leading edge | Hedonic |

## Key Results (Paired t-Tests)

This analysis compared the Museum system with the Baseline system across usability and user experience metrics. The results indicate statistically significant improvements for the Museum condition across all evaluated dimensions.

| **Metric**     | **t-statistic** | **p-value** | **Interpretation** |
|----------------|-----------------|-------------|--------------------|
| SUS            | 5.84            | < .001      | Significant improvement in perceived usability |
| UEQ Pragmatic  | 34.14           | < .001      | Strong improvement in pragmatic quality and effectiveness |
| UEQ Hedonic    | 38.46           | < .001      | Strong improvement in hedonic quality and stimulation |
