import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

class ResumeApp:
    def __init__(self, root):
        root.title("David Harris - Resume")
        root.geometry("1400x900")
        root.configure(bg="#0f0f0f")
        root.option_add('*Font', ('Segoe UI', 10))

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background="#0f0f0f")
        style.configure("TLabel", background="#0f0f0f", foreground="#f0f0f0", font=("Segoe UI", 11))
        style.configure("Title.TLabel", foreground="#00bcd4", font=("Segoe UI", 22, "bold"))
        style.configure("Section.TLabel", foreground="#00bcd4", font=("Segoe UI", 14, "bold"))
        style.configure("Card.TFrame", background="#1c1c1c", relief="flat", borderwidth=0)

        canvas = tk.Canvas(root, bg="#0f0f0f", highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_mouse_wheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        content_frame.bind("<Configure>", on_configure)
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        sidebar = ttk.Frame(content_frame, width=300)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="ns", padx=(20, 10), pady=20)

        try:
            profile_img = Image.open("profile.jpg").resize((160, 160))
            mask = Image.new('L', (160, 160), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 160, 160), fill=255)
            profile_img.putalpha(mask)
            profile_photo = ImageTk.PhotoImage(profile_img)
            profile_label = tk.Label(sidebar, image=profile_photo, bg="#0f0f0f")
            profile_label.image = profile_photo
            profile_label.pack(pady=10)
        except:
            tk.Label(sidebar, text="[No Image]", bg="#0f0f0f", fg="#bbb").pack(pady=10)

        ttk.Label(sidebar, text="Chukwuebuka David Harris", style="Title.TLabel", wraplength=280).pack(pady=5)
        ttk.Label(sidebar, text="Newport - Gwent, NP19 4AN\nUnited Kingdom\n+44 7903342754\ndavidharris200111@gmail.com\nGithub.io/Resume", wraplength=280, justify="center").pack(pady=10)

        resume_frame = ttk.Frame(content_frame)
        resume_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)

        sections = [
            ("Professional Summary", "I am a driven and enthusiastic Computer Science graduate looking for an opportunity to contribute my expertise in software development, IT services, and analytical thinking. I have a genuine passion for technology and a strong desire to gain real-world experience in a dynamic work setting. Known for being a reliable team player with solid leadership abilities, adaptability, and a forward-thinking mindset. I bring hands-on experience in delivering quality technical support and effectively troubleshooting to maintain smooth IT operations. Resourceful in identifying and resolving both hardware and software problems efficiently. I am skilled in clear communication, especially when translating technical ideas into user-friendly explanations."),
            ("Career Goals", "Gain hands-on experience in software, mobile, and web development while enhancing problem-solving and analytical skills. Develop expertise in AI, machine learning, and emerging technologies to contribute to innovative tech solutions."),
            ("Experience", "WORK EXPERIENCE\n\n06/2025 – Current Data Analyst\nDigital Echoes – London, UK\n• Analyzed datasets from Google Analytics and Excel to identify trends in sessions, users, and acquisition channels.\n• Created reusable Power BI templates and Excel visuals for consistent reporting and dashboard updates.\n• Assisted in data formatting, testing, and integration across tools to ensure clean transitions and clear outputs.\n• Managed data access and supported peers in troubleshooting data display and metric calculation issues.\n• Reviewed performance metrics and built tracking for KPIs like session growth and country distribution.\n• Produced structured reports that guided insights on resource placement and performance trends.\n\n06/2024 to 12/2025 IT Technical Analyst\nAdventus IT Services (Philippines) Inc. - Makati, Metro Manila, Philippines\n• Provided first-level technical support and resolved hardware, software, and network-related issues to minimize system downtime.\n• Conducted system diagnostics and assisted in implementing solutions aligned with organizational IT standards.\n• Collaborated with software developers to test applications, document bugs, and verify feature enhancements.\n• Analyzed user requirements and contributed to system upgrades and process improvements.\n• Created and maintained technical documentation, including system specifications and configuration guides.\n• Participated in IT projects by gathering data, supporting deployments, and conducting post-implementation reviews.\n• Assisted with the configuration and management of mobile and remote-access solutions to support a hybrid workforce.\n• Supported IT asset management through inventory tracking and usage reporting."),
            ("Training", "TRAINING COURSE\n04/2025 Data Analyst – Advance Careers UK\nTopics covered:\n• Data preprocessing\n• Descriptive statistics\n• Regression analysis\n• Data visualization using charts and PivotTables\n• Excel functions like SUMIF, filtering, and conditional formatting\n• Introduction to machine learning techniques\n• Real-world applications in pharmaceutical and business data\nProjects:\n• Sales performance analysis using Excel\n• Predictive modeling using linear regression on pharmaceutical data\n• Dashboard creation for summarizing large datasets"),
            ("Tech Stack/Skills", [
                ["Java", "C", "C++", "C#", "HTML"],
                ["CSS", "JavaScript", "Python", "MySQL", "Data Analysis"],
                ["Troubleshooting", "vSphere", "vCenter", "Azure", "Active Directory"]
            ]),
            ("Skill Proficiency", [
                ("Java", 85),
                ("Python", 80),
                ("IT Troubleshooting", 90),
                ("Networking", 75)
            ]),
            ("Tools", [
                ["Power BI", "Excel", "VirtualBox"],
                ["VMware", "Wireshark", "FTK Imager"],
                ["Kali Linux", "Firebase", "Postman"]
            ]),
            ("Education", "BSc Computer Science – Arellano University (2025)\nSenior High – Kings Senior HS (2017)..."),
            ("Certifications", "CC Domain 1-4: Security, IR & BCDR, Access Control, Network Security – (ISC)² Valid Jan 2025 – Jan 2028"),
            ("Projects", [
                ["Smart Destination Alert System", "Document Tracking System", "File Management System"],
                ["Ticket Management System", "Arduino Robot Car", "PC Build"],
                ["HTML/PHP Websites"]
            ]),
            ("Portfolio", "Downloadable portfolio available upon request."),
            ("Experience Timeline", "2025–Present: Data Analyst – Digital Echoes\n2024–2025: IT Technical Analyst – Adventus"),
            ("Testimonials", "\"David’s attention to detail and ability to troubleshoot under pressure made him an asset...\" – Former Supervisor\n\"One of the most resourceful and reliable analysts I’ve worked with.\" – Manager"),
            ("Gallery", "Project screenshots available upon request.")
        ]

        for i, (heading, content) in enumerate(sections):
            section = tk.Frame(resume_frame, bg="#1c1c1c", bd=0, highlightbackground="#333", highlightthickness=2)
            section.grid(row=i, column=0, pady=10, sticky="ew", padx=5)
            section.columnconfigure(0, weight=1)

            ttk.Label(section, text=heading, style="Section.TLabel").grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))

            if isinstance(content, str):
                ttk.Label(section, text=content, wraplength=1000, justify="left").grid(row=1, column=0, sticky="w", padx=10, pady=(0, 10))
            elif isinstance(content, list):
                if heading == "Skill Proficiency":
                    for idx, (skill, percent) in enumerate(content):
                        ttk.Label(section, text=skill).grid(row=1 + idx*2, column=0, sticky="w", padx=10)
                        progress = ttk.Progressbar(section, length=400, value=percent)
                        progress.grid(row=2 + idx*2, column=0, sticky="w", padx=10, pady=(0, 5))
                else:
                    col_frame = tk.Frame(section, bg="#1c1c1c")
                    col_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
                    for col in content:
                        ul = tk.Frame(col_frame, bg="#1c1c1c")
                        ul.pack(side="left", expand=True, fill="both", padx=10)
                        for item in col:
                            tk.Label(ul, text="• " + item, anchor="w", justify="left", bg="#1c1c1c", fg="#f0f0f0", font=("Segoe UI", 11)).pack(anchor="w")

        resume_frame.columnconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()
