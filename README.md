# 📊 Freshers Hiring Trends in India – Exploratory Data Analysis

## 📌 Project Overview

This project focuses on analyzing **Freshers Hiring Trends in India** using Exploratory Data Analysis (EDA).

The objective is to understand the factors associated with fresher hiring outcomes and salary patterns. The analysis explores candidate-related attributes such as **CGPA, internships, projects, certifications, skills, educational qualification, hiring stage, industry sector, and offered salary**.

The project uses Python-based data analysis and visualization techniques to identify meaningful patterns and generate actionable insights for both job seekers and recruiters.

---

## 🎯 Problem Statement

Companies receive a large number of applications from freshers, but it can be difficult to understand which candidate attributes are associated with different stages of the hiring process and salary outcomes.

This project analyzes fresher hiring data to identify patterns and relationships between:

- Academic performance
- Internship experience
- Projects
- Certifications
- Skills
- Educational qualifications
- Hiring stages
- Industry sectors
- Offered salary

---

## 🎯 Objectives

The major objectives of this project are:

- Analyze fresher hiring trends in India.
- Understand the factors associated with hiring outcomes.
- Analyze the relationship between CGPA and hiring stages.
- Study the role of internship experience in the hiring process.
- Analyze salary patterns across educational qualifications and industry sectors.
- Identify meaningful patterns using exploratory data analysis.
- Provide recommendations based on the findings.

---

## 📂 Dataset

The dataset contains:

- **5,000 candidate records**
- **30 features**

The dataset includes information related to:

- Candidate demographics
- Educational qualifications
- CGPA
- Backlogs
- Internship experience
- Number of projects
- Certifications
- Skills
- Applications
- Hiring stages
- Interview rounds
- Industry sector
- Job role
- Offered salary
- LinkedIn activity
- Referrals

---

## 🛠️ Technologies & Tools Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Environment
- Jupyter Notebook / Google Colab

---

## 🔄 Project Workflow

The project follows the following EDA workflow:

1. **Data Collection**
2. **Data Loading**
3. **Data Understanding**
4. **Data Cleaning**
5. **Missing Value Analysis**
6. **Univariate Analysis**
7. **Bivariate Analysis**
8. **GroupBy Analysis**
9. **Crosstab Analysis**
10. **Pivot Table Analysis**
11. **Data Visualization**
12. **Insight Generation**
13. **Recommendations**

---

## 🧹 Data Cleaning

The following data-cleaning steps were performed:

- Checked dataset shape and structure.
- Examined column names and data types.
- Generated descriptive statistics.
- Identified missing values.
- Handled missing values based on the respective columns.
- Rechecked the dataset after cleaning before performing further analysis.

Missing values were primarily observed in columns such as:

- Interview Rounds
- Offered Salary
- LinkedIn Premium

For the analysis, missing interview-round and offered-salary values were handled as `0`, while missing LinkedIn Premium values were represented as `Unknown`.

---

## 📊 Exploratory Data Analysis

### 1. Univariate Analysis

Individual variables were analyzed to understand their distributions.

Examples include:

- Gender distribution
- CGPA distribution
- Internship experience
- Number of projects
- Certifications
- Hiring stages
- Industry sectors
- Offered salary

---

### 2. GroupBy Analysis

GroupBy analysis was used to compare numerical metrics across different categories.

For example:

**Average CGPA by Hiring Stage**

This helped understand how academic performance varied across different stages of the hiring process.

---

### 3. Crosstab Analysis

Crosstab analysis was used to study relationships between categorical variables.

For example:

**Prior Internship Experience vs Hiring Stage**

This helped understand how candidates with and without internship experience were distributed across the hiring process.

---

### 4. Pivot Table Analysis

Pivot tables were used to analyze salary patterns across multiple categories.

For example:

**Average Offered Salary by Degree and Industry Sector**

This helped identify differences in salary across various combinations of educational qualifications and industry sectors.

---

## 🔍 Key Insights

### 📌 Insight 1 – CGPA and Hiring Stage

The analysis showed differences in average CGPA across hiring stages.

Candidates in some advanced hiring stages had slightly higher average CGPAs compared with candidates in earlier or rejected stages.

This indicates that academic performance can be a relevant factor during the hiring process, particularly during screening and shortlisting.

---

### 📌 Insight 2 – Internship Experience

Internship experience was analyzed across different hiring stages.

The analysis indicates that internship experience can provide candidates with practical exposure and may be considered an indicator of job readiness.

---

### 📌 Insight 3 – Education, Sector and Salary

Salary varied based on the combination of:

- Educational qualification
- Industry sector

Certain degree-sector combinations showed higher average salary levels than others.

This indicates that salary outcomes can depend not only on the degree a candidate holds but also on the industry sector in which they apply.

---

## 💡 Recommendations

Based on the analysis, the following recommendations can be made:

### For Freshers

- Maintain a good academic record.
- Gain practical experience through internships.
- Build relevant academic and personal projects.
- Develop skills aligned with the target job role.
- Choose certifications that complement the desired career path.
- Research industry sectors and salary patterns before applying.

### For Recruiters

- Consider multiple candidate attributes instead of relying on a single factor.
- Evaluate candidates based on a combination of academics, internships, projects and relevant skills.
- Use data-driven insights to improve fresher screening and hiring processes.

---

## 📈 Business Decisions

The analysis can support the following decisions:

- Improve fresher candidate screening.
- Identify important candidate attributes for hiring.
- Understand salary differences across sectors and educational backgrounds.
- Help freshers identify areas for profile improvement.
- Support better career and industry-selection decisions.

---

## 🏁 Conclusion

This project demonstrates how **Exploratory Data Analysis can be used to analyze fresher hiring trends and extract meaningful insights from recruitment data**.

The analysis highlighted the importance of factors such as **CGPA, internship experience, educational qualification, projects and skills**, while also showing that salary patterns can vary across different industry sectors and educational backgrounds.

Overall, the project helped transform raw hiring data into useful insights that can support **better career decisions for freshers and more informed hiring decisions for recruiters**.

---

## 🚀 Future Improvements

If further developed, this project could be enhanced by:

- Building an interactive dashboard using **Power BI or Streamlit**.
- Performing deeper statistical analysis.
- Analyzing relationships between skills and hiring outcomes.
- Building predictive models for hiring outcomes.
- Developing a salary prediction model.
- Adding more recent fresher hiring data.

---

## 👩‍💻 Skills Demonstrated

Through this project, I demonstrated practical knowledge of:

- Python
- Pandas
- NumPy
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- GroupBy
- Crosstab
- Pivot Tables
- Matplotlib
- Seaborn
- Insight Generation
- Business Recommendations

---

## 📁 Project Structure

```text
Freshers-Hiring-Trends-India/
│
├── EDA_project.ipynb
├── dataset/
│   └── fresher_hiring_data.csv
├── images/
│   └── analysis_charts.png
└── README.md
