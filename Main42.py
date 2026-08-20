# M11.Implement a Classification/Logistic Regression Problem. For Example Based on Different Features of Students Data, Classify, Whether a Student is Suitable for a Particular Activity. Based on the Available Dataset, a Student can Also Implement Another Classification Problem Like Checking Whether an Email is Spam or Not.
import numpy as np;
from sklearn.linear_model import LogisticRegression;
# =====================================================
# Q11 - LOGISTIC REGRESSION / CLASSIFICATION.
# =====================================================
# -----------------------------------------------------
# 1. STUDENT CLASSIFICATION.
# -----------------------------------------------------
# Features :
# Study Hours, Attendance, Marks.
X_student = np.array(
    [
        [2, 60, 45],
        [3, 65, 50],
        [4, 70, 55],
        [5, 75, 65],
        [6, 80, 70],
        [7, 85, 80],
        [8, 90, 90],
    ]
)
# 0 = Not Suitable.
# 1 = Suitable.
y_student = np.array([0, 0, 0, 1, 1, 1, 1])
# Create and Train Model.
student_model = LogisticRegression()
student_model.fit(X_student, y_student)
# New Student.
# Study Hours = 6.
# Attendance = 82.
# Marks = 75.
student = np.array([[6, 82, 75]])
prediction = student_model.predict(student)
print("===== STUDENT CLASSIFICATION =====")
if prediction[0] == 1:
    print("Student is Suitable.")
else:
    print("Student is Not Suitable.")
# -----------------------------------------------------
# 2. SPAM EMAIL CLASSIFICATION.
# -----------------------------------------------------
# Features :
# Number of Links, Number of Words.
X_email = np.array([[1, 20], [2, 25], [1, 30], [10, 15], [12, 10], [15, 12]])
# 0 = Not Spam.
# 1 = Spam.
y_email = np.array([0, 0, 0, 1, 1, 1])
# Create and Train Model.
email_model = LogisticRegression()
email_model.fit(X_email, y_email)
# New Email.
# Links = 12.
# Words = 15.
email = np.array([[12, 15]])
prediction = email_model.predict(email)
print("\n===== EMAIL CLASSIFICATION =====")
if prediction[0] == 1:
    print("Spam Email.")
else:
    print("Not Spam Email.")