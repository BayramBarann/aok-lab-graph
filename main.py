import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from tkinter import filedialog

def grafigi_ciz():
    try:
        # 1. Kullanıcıdan Verileri Al ve Temizle
        x_girdi = entry_x_veri.get()
        y_girdi = entry_y_veri.get()
        
        # Virgüllerden böl, boşlukları temizle ve ondalıklı sayıya (float) çevir
        x_listesi = [float(deger.strip()) for deger in x_girdi.split(',')]
        y_listesi = [float(deger.strip()) for deger in y_girdi.split(',')]
        
        # X ve Y veri sayılarının eşit olup olmadığını kontrol et
        if len(x_listesi) != len(y_listesi):
            messagebox.showerror("Veri Uyuşmazlığı", f"X ekseni için {len(x_listesi)}, Y ekseni için {len(y_listesi)} veri girdiniz.\nVeri sayıları eşit olmalıdır!")
            return
            
        x = np.array(x_listesi)
        y = np.array(y_listesi)

        # 2. Metin Girdilerini Al
        baslik = entry_baslik.get() or "Genel Doğrusal Regresyon"
        x_isim = entry_x_isim.get() or "X Ekseni"
        y_isim = entry_y_isim.get() or "Y Ekseni"

        # 3. Doğrusal Regresyon Hesaplaması
        slope, intercept, r_value, _, _ = linregress(x, y)
        r_squared = r_value**2

        # 4. Grafik Çizim Ayarları (AOK LAB Teması)
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(9, 6))
        fig.patch.set_facecolor('#0d1117')
        ax.set_facecolor('#0d1117')
        fig.subplots_adjust(right=0.70, bottom=0.12)

        
        # Veri ve Doğru Çizimi
        ax.plot(x, y, marker='o', markersize=8, color='cyan', linestyle='None', label='Deneysel Veriler')
        ax.plot(x, intercept + slope * x, color='#3b82f6', linestyle='-', linewidth=2, label='Doğrusal Regresyon')

        eq_text = f"y = {slope:.4f}x + {intercept:.4f}\n$R^2$ = {r_squared:.4f}\nEğim ($m$) = {slope:.4f}"
        ax.text(1.04, 1.0, eq_text, transform=ax.transAxes, fontsize=11, verticalalignment='top',
                bbox=dict(facecolor='#161b22', edgecolor='cyan', alpha=0.8, boxstyle='round,pad=0.5'), color='white')

# 3. Filigran ve İmza (Görselin en sağ altına kaydırıldı ve hizalandı)
        fig.text(0.98, 0.04, 'AOK LAB', fontsize=18, color='cyan', 
                 alpha=0.6, ha='right', va='bottom', weight='bold')

        fig.text(0.98, 0.015, 'made by bayram baran yeşil', fontsize=9, color='cyan', 
                 alpha=0.4, ha='right', va='bottom', style='italic')
# Eksen ve Başlık Ayarları
        ax.set_xlabel(x_isim, fontsize=12, color='white', weight='bold')
        ax.set_ylabel(y_isim, fontsize=12, color='white', weight='bold')
        ax.set_title(baslik, fontsize=14, color='white', weight='bold')
        ax.tick_params(colors='white')
        ax.grid(True, linestyle='--', alpha=0.2, color='white')
        
# Lejant (Sol alt köşeye taşındı)
        ax.legend(bbox_to_anchor=(1.04, 0.60), loc='upper left', facecolor='#161b22', edgecolor='cyan')
        ax.grid(True, linestyle='--', alpha=0.2, color='white')

        # 5. Kaydet ve Göster
        dosya_adi = "AOK_Genel_Grafik.png"
        plt.savefig(dosya_adi, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        
        messagebox.showinfo("Başarılı", f"Grafik çizildi ve '{dosya_adi}' adıyla bulunduğunuz klasöre kaydedildi.")
        plt.show()

    except ValueError:
        messagebox.showerror("Format Hatası", "Lütfen verileri sadece sayısal formatta ve aralarına virgül koyarak girin.\n(Ondalık kısımlar için nokta kullanın. Örn: 1.2, 3.5, 4)")
    except Exception as e:
        messagebox.showerror("Beklenmeyen Hata", f"Bir sorun oluştu:\n{str(e)}")


    dosya_yolu = filedialog.asksaveasfilename(
        title="Grafiği Kaydet",
        defaultextension=".png",
        initialfile="AOK_Genel_Grafik.png",
        filetypes=[("PNG Görseli", "*.png")]
    )

    if not dosya_yolu:
        plt.close(fig)
        return

    fig.savefig(
        dosya_yolu,
        dpi=300,
        bbox_inches="tight",
        facecolor=fig.get_facecolor()
    )

    messagebox.showinfo(
        "Başarılı",
        f"Grafik kaydedildi:\n{dosya_yolu}"
    )

    plt.show()

# ==========================================
# --- GUI (Arayüz) OLUŞTURMA BÖLÜMÜ ---
# ==========================================
root = tk.Tk()
root.title("AOK LAB - Veri Analiz ve Grafik Aracı")
root.geometry("450x450")
root.configure(padx=20, pady=20)

# Ortak font ayarı
font_ayari = ("Arial", 10, "bold")

# Başlık Girdisi
tk.Label(root, text="Grafik Başlığı:", font=font_ayari).pack(anchor="w", pady=(0, 2))
entry_baslik = tk.Entry(root, width=50)
entry_baslik.pack(pady=(0, 10))

# X Ekseni İsim Girdisi
tk.Label(root, text="X Ekseni Etiketi:", font=font_ayari).pack(anchor="w", pady=(0, 2))
entry_x_isim = tk.Entry(root, width=50)
entry_x_isim.pack(pady=(0, 10))

# Y Ekseni İsim Girdisi
tk.Label(root, text="Y Ekseni Etiketi:", font=font_ayari).pack(anchor="w", pady=(0, 2))
entry_y_isim = tk.Entry(root, width=50)
entry_y_isim.pack(pady=(0, 10))

# X Verileri Girdisi
tk.Label(root, text="X Verileri (Virgülle ayırın, örn: 1, 2, 3.5, 4):", font=font_ayari).pack(anchor="w", pady=(0, 2))
entry_x_veri = tk.Entry(root, width=50)
entry_x_veri.pack(pady=(0, 10))

# Y Verileri Girdisi
tk.Label(root, text="Y Verileri (Virgülle ayırın, örn: 10, 20.5, 30, 42):", font=font_ayari).pack(anchor="w", pady=(0, 2))
entry_y_veri = tk.Entry(root, width=50)
entry_y_veri.pack(pady=(0, 20))

# Çizim Butonu
btn_ciz = tk.Button(root, text="Grafiği Çiz ve Kaydet", bg="#3b82f6", fg="white", font=("Arial", 12, "bold"), command=grafigi_ciz)
btn_ciz.pack(fill="x", pady=10)

# Arayüzü Başlat
root.mainloop()