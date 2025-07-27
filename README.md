

# DTO Generator – Flask + Spring Boot Integration

## 📖 Overview

This project demonstrates how to **automatically generate Java DTO classes** from simple text requirements using **Google Gemini (Generative AI)**.
It consists of:

* ✅ A **Flask service** (Python) using Gemini API to generate DTOs.
* ✅ A **Spring Boot service** that calls the Flask API and returns the DTO to the client.

This is useful for automating boilerplate DTO creation in Java projects.

---

## 🛠 **Tech Stack**

* **Python 3.10+ / Flask** – REST API for DTO generation
* **Google Gemini (Generative AI)** – AI model to generate DTOs
* **Spring Boot 2.7+ (Java)** – Consumes Flask API and exposes an endpoint
* **Postman** – For testing endpoints
* **Git / GitHub** – Version control

---

## 🚀 **Features**

✔ Generate clean Java DTO classes with fields, constructors, getters, and setters
✔ Customizable class name and fields
✔ Uses environment variable for `GOOGLE_API_KEY` (secure, no hardcoding)
✔ Saves the generated DTO as a `.java` file
✔ Integrated with Spring Boot for enterprise use

---

## ⚙ **Setup Instructions**

### ✅ **1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/dto-generator.git
cd dto-generator
```

---

### ✅ **2. Setup Flask Service (Python)**

#### **Install Requirements**

```bash
pip install flask google-generativeai python-dotenv
```

#### **Set Google API Key**

**Option A: Environment Variable (Recommended)**

* **Windows (CMD or PowerShell):**

```cmd
set GOOGLE_API_KEY=your_actual_key
```

* **Linux / Mac:**

```bash
export GOOGLE_API_KEY="your_actual_key"
```

Check:

```cmd
echo %GOOGLE_API_KEY%    # Windows
echo $GOOGLE_API_KEY     # Linux/Mac
```

---

**Option B: `.env` File (Easy for Local Development)**

1. Create a `.env` file in the project folder:

```
GOOGLE_API_KEY=your_actual_key
```

2. The Flask code will automatically pick it up (using `python-dotenv`).

---

#### **Run Flask Service**

```bash
python dto_flask_service.py
```

The service will run at:
`http://localhost:5000/generate-dto`

---

### ✅ **3. Setup Spring Boot (Java)**

1. Open the Maven project in **Spring Tool Suite (STS)** or IntelliJ.
2. Ensure `RestTemplate` is configured properly to call Flask:

```java
String flaskUrl = "http://localhost:5000/generate-dto";
```

3. Run as **Spring Boot App**:

```
Tomcat started on port(s): 8080
```

The Spring Boot API will run at:
`http://localhost:8080/api/generate-dto`

---

## 🧪 **API Testing (Postman)**

### **Flask Endpoint**

**POST URL:**

```
http://localhost:5000/generate-dto
```

**Body (raw JSON):**

```json
{
  "className": "OrderDetailsDTO",
  "requirement": "orderId(Long), customerName(String), totalAmount(Double)"
}
```

**Sample Response:**

```json
{
  "dto": "public class OrderDetailsDTO { ... }",
  "savedFile": "OrderDetailsDTO.java"
}
```

---

### **Spring Boot Endpoint**

**POST URL:**

```
http://localhost:8080/api/generate-dto
```

**Body (raw JSON):**

```json
{
  "className": "OrderDetailsDTO",
  "requirement": "orderId(Long), customerName(String), totalAmount(Double)"
}
```

**Sample Response:**

```java
public class OrderDetailsDTO {
    private Long orderId;
    private String customerName;
    private Double totalAmount;

    public OrderDetailsDTO() {}
    public OrderDetailsDTO(Long orderId, String customerName, Double totalAmount) {
        this.orderId = orderId;
        this.customerName = customerName;
        this.totalAmount = totalAmount;
    }

    public Long getOrderId() { return orderId; }
    public void setOrderId(Long orderId) { this.orderId = orderId; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }
    public Double getTotalAmount() { return totalAmount; }
    public void setTotalAmount(Double totalAmount) { this.totalAmount = totalAmount; }
}
```

---

## 🔮 **Future Enhancements**

* ⬜ Return `.java` file as a downloadable response directly
* ⬜ Add authentication for secure access
* ⬜ Support nested DTO generation
* ⬜ Create a web UI to input class name and fields

---

## 🧑‍💻 **Author**

**Gayathri Nuguri**
*(Software Engineer – Java & Spring Boot)*

---

## ⭐ **Contributions**

Contributions are welcome! Fork this repo, make changes, and raise a pull request.

---

## 📜 **License**

This project is licensed under the MIT License.

---

### ✅ **Next Steps for You**

1. **Copy all of the above into a `README.md` file** in your project folder.
2. Run these commands to push it:

```bash
git add README.md
git commit -m "Added complete README"
git push
```


