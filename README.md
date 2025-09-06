#  DiagnoGraph: Streamlit-Based Patient Health Diagnosis Report

**DiagnoGraph** is a healthcare data analysis and visualization tool designed to help doctors and patients track health trends over time. It provides **interactive Streamlit dashboards** with patient-specific records, BMI calculation, and summary-based health status classification using graphs and values.  

---

##  Features  

-  **Streamlit Dashboard** for interactive visualization  
-  **Patient-specific analysis** – Enter a patient ID to view their data only  
-  **Standardized data plots** for accurate comparisons  
-  **Summary Report** including:  
  -  BMI (shown at the beginning and in the summary)  
  -  Values of multiple medical tests                                         #Under Progress
  -  Final health status (Healthy / At Risk)
  -  Predicted disease (if detected)                                          #Under Progress

---

##  Project Structure  

-  Main Streamlit application (frontend + visualization)  
-  Backend(Standardization and preprocessing  )
-  Graph generation  

---

##  Project Images  

<img width="800" height="400" alt="Screenshot 2025-09-03 053823" src="https://github.com/user-attachments/assets/b5604580-248c-4c54-9f09-6f26bd45bb60" />
<img width="800" height="400" alt="Screenshot 2025-09-03 053838" src="https://github.com/user-attachments/assets/359871c2-3e82-4831-93ca-0f39f8ed67b5" />
<img width="800" height="400" alt="Screenshot 2025-09-03 053854" src="https://github.com/user-attachments/assets/5b7e6939-60d3-4ee6-acbf-c871ac2f27ac" />
<img width="800" height="400" alt="Screenshot 2025-09-03 053908" src="https://github.com/user-attachments/assets/347e2fdf-6f1c-4f25-b91f-7b5bc1ae5731" />
<img width="800" height="400" alt="Screenshot 2025-09-03 053922" src="https://github.com/user-attachments/assets/e8bedd0b-e00a-441c-9961-bd66ba1a2cfb" />
<img width="800" height="400" alt="Screenshot 2025-09-03 053930" src="https://github.com/user-attachments/assets/a3681b30-51ab-45a3-9e1b-f762faef23c4" />

- Streamlit dashboard  
- Patient graphs  
- Summary report with BMI and health status  

---

##  Tech Stack  

-  **Streamlit** — Interactive dashboard framework  and plotting Graphs
-  **Python 3.10+** — Main programming language  
-  **NumPy & Pandas** — Data handling and standardization
  
---

##  Getting Started  

###  Prerequisites  
- Python 3.10+    
- Required Python packages (listed in `requirements.txt`)  

---

###  Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Sai-Deepan/DiagnoGraph.git
   cd DiagnoGraph
2.Install required Python packages:
-pip install -r requirements.txt

3. Feed the CSV files

###  Usage Displays graphs of different test results

 Generates summary with BMI and test values

 Shows health status (Healthy / At Risk)

 Predicts potential disease if health deviates from normal                    #Under progress


1.Start the Streamlit application:

streamlit run app.py

2.Enter a patient ID in the interface.

3.Visualise the data and summarise the report


##  Why DiagnoGraph?  

Monitoring health over time is critical. **DiagnoGraph** combines **data standardization, visualization, and health summarization** with a simple **Streamlit interface**, making it easier for doctors and patients to:  

-  **Track progress**  
-  **Understand health status**  
- **Make informed decisions**

## Contributors:
## 1)Deepan Sai
## 2)Aadithya V
## 3)Viswasainath Vijayakumar
## 4)Deepak R
