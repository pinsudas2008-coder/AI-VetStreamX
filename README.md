# AI-VetStreamX 
# AI-VetStreamX 🐾

AI-VetStreamX เป็นระบบวินิจฉัยโรคผิวหนังสัตว์เลี้ยงแบบ *AI-assisted* สำหรับสุนัขและแมว โดยใช้การวิเคราะห์ภาพด้วย *Deep Learning (ResNet18)* และ metadata ของสัตว์ เพื่อให้ผลวินิจฉัยเบื้องต้น พร้อม Heatmap (Grad-CAM) แสดงบริเวณที่ AI ให้ความสำคัญในภาพ  

โปรเจกต์นี้พัฒนาขึ้นโดยนักเรียนมัธยมปลายผู้มีใจรักนวัตกรรม เพื่อส่งเสริมการศึกษาและการวิจัยด้านสุขภาพสัตว์


---

## *📌 จุดเด่นของระบบ*

- วิเคราะห์โรคผิวหนังสัตว์แบบเบื้องต้น (สุนัข/แมว)
- รองรับข้อมูล *ประเภทสัตว์, อายุ, เพศ, โรคประจำตัว, ระยะเวลามีอาการ* และ *ภาพผิวหนังสัตว์*
- แสดง *ผลวิเคราะห์เบื้องต้น 3 อันดับ + ความมั่นใจ (%)*
- แสดง *Grad-CAM Heatmap* บนภาพจริง
- Dashboard สถิติผู้ใช้งานและโรคที่ตรวจพบ
- Knowledge Hub ให้ข้อมูลวิชาการสัตวแพทย์และคำแนะนำเบื้องต้น
- รองรับ *export CSV* สำหรับงานวิจัย
## *📂 โครงสร้างโปรเจกต์*

AI-VetStreamX/
├─ web/                   # หน้า Streamlit app
│  ├─ app.py
│  └─ pages/
│     ├─ home.py
│     ├─ diagnosis.py
│     ├─ dashboard.py
│     └─ knowledge.py
├─ src/                   # โมดูล AI และ Data Handling
│  ├─ dataset.py
│  ├─ train.py
│  └─ inference.py
├─ models/                # เก็บโมเดล ResNet18 ที่เทรนแล้ว
├─ data/                  # Dataset (Train/Val/Test)
│  ├─ train/
│  │  ├─ Cat/
│  │  └─ Dog/
│  ├─ val/
│  └─ test/
├─ requirements.txt       # ไลบรารีที่ต้องติดตั้ง
└─ README.md 


## *⚙️ วิธีติดตั้งและรันระบบ*

1. *สร้าง virtual environment*
```bash
python -m venv venv
2.	Activate venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# macOS / Linux
source venv/bin/activate
#	3.	ติดตั้งไลบรารี
pip install -r requirements.txt

4. run เข้าเว็บคำสั่ง
streamlit run web/app.py


5.	เข้าชมแอป

	•	Local URL: http://localhost:8501
📈 การใช้งานแต่ละหน้า

1. Home
	
	•	ปุ่ม “เริ่มวิเคราะห์โรค” → ไปยังหน้า Diagnosis
	•	เมนูด้านบน: คู่มือการใช้งาน / เกี่ยวกับเรา / ศูนย์ความรู้
	•	ข้อความเตือน: ผลวิเคราะห์เบื้องต้นเท่านั้น

2. AI Diagnosis
	•	กรอกข้อมูลสัตว์: ประเภทสัตว์, อายุ, เพศ, โรคประจำตัว, ระยะเวลามีอาการ
	•	อัปโหลดภาพผิวหนังสัตว์
	•	ปุ่ม Analyze Now → แสดงผลวิเคราะห์
	•	แสดง Top 3 โรค + % ความมั่นใจ
	•	Heatmap แสดงบริเวณที่ AI ให้ความสำคัญ
	•	ข้อความแนะนำและเตือน

3. Dashboard
	•	แสดงกราฟและสถิติผู้ใช้งาน
	•	กรองข้อมูล: ประเภทสัตว์ / ช่วงเวลา / อายุสัตว์
	•	Export CSV สำหรับงานวิจัย

4. Knowledge Hub
	•	ให้ข้อมูลการดูแลสัตว์และโรคผิวหนัง
	•	ระบบค้นหาและการแนะนำ (สำหรับรุ่นถัดไปสามารถเพิ่ม Chatbot)


