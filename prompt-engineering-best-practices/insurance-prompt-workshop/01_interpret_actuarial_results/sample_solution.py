challenge_1_1_sample_solution = """
Here is an actuarial data set in CSV format:

<data>
{$ACTUARIAL_DATA}
</data>

Please carefully analyze this data, looking closely at each individual column as well as the
relationships and correlations between different columns.

Write your initial analysis, observations and thoughts in a <scratchpad> section before preparing
your final interpretation.

<scratchpad>
</scratchpad>

Now, please provide a detailed but easy-to-understand written interpretation of what this data is
showing. Write this in an <interpretation> section.

Your interpretation should cover:
- The key insights, trends and takeaways you see in the data
- An explanation of any important outliers, anomalies or unexpected results
- Information from the data that would be most relevant, interesting and actionable for
non-actuarial business functions, such as sales, marketing, product development, etc. Think about
what they would need to know.

Please avoid using overly technical actuarial terminology or jargon in your interpretation. Explain
things in a way a non-actuary can understand.

"""

challenge_1_2_sample_solution = """
You are an AI assistant skilled in data analysis and SQL. I will provide you with an actuarial data
set in the following format:

<actuarial_data>
{$ACTUARIAL_DATA}
</actuarial_data>

Your task is to write a SQL query that calculates the average A/E ratio (a_over_e column) separately
for the smoker and non-smoker groups. Your query should return the higher of the two average values.

Before writing your final query, think through the problem and plan out your approach in a
<scratchpad> section. Consider what tables you need to access, what columns you need to select, how
to group the data, and how to compare the averages to return the higher value.

After planning your approach, write your final SQL query inside <query> tags.

Finally, explain how your query works and interprets the result inside <explanation> tags. Discuss
how you grouped and aggregated the data, how you compared the smoker vs non-smoker averages, and
what the final result represents.

Remember, the goal is to returna single value representing the higher of the average A/E ratios
between the smoker and non-smoker populations in this actuarial data set. Carefully consider the
logic needed in your SQL to achieve this.
"""

challenge_1_3_sample_solution = 
""" You will be acting as an actuarial consultant analyzing an actuarial data set for an insurance
company. The data set will be provided in the following format:

<actuarial_data>
{$ACTUARIAL_DATA}
</actuarial_data>

The data has the following columns:
policy_id, age, gender, smoker, policy_duration, actual_mortality_rate, expected_mortality_rate,
a_over_e, coverage, premium

Your task is to carefully analyze this data, paying particular attention to the coverage, a_over_e
(a_e_ratio), and premium columns. Look for any concerning patterns, such as policies that seem to be
underpriced or overpriced given their risk characteristics.

First, in a <reasoning> section, share your detailed analysis of the data. Discuss any notable
patterns or concerns you observe with the coverage, a_e_ratio, and premium. Explain your thought
process and the actuarial principles you are applying.

Then, in a <recommendations> section, summarize your key recommendations for the insurance company
based on your analysis. Should they consider adjusting premiums for certain policies? Are there any
risk segments that warrant further investigation? Provide clear and actionable guidance.

Remember, as an actuarial consultant, it's your job to apply your expertise to ensure this insurance
product is sustainably priced and managed. Let me know if you have any other questions!"""
