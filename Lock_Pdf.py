import pikepdf

print("===== HariPrabodham ======")

# Open the original PDF
old_pdf = pikepdf.Pdf.open("1.pdf")

# Set permissions to disallow extraction
no_extr = pikepdf.Permissions(extract=False)

# Save the new PDF with encryption
old_pdf.save("hp.pdf", encryption=pikepdf.Encryption(user="hp369", owner="HP", allow=no_extr))