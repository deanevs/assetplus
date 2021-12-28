asset_id = row['asset'].strip()
details = {
    "serial": row['serial'].strip(),
    "manufacturer": row['manu'].strip(),
    "model": row['model'].strip(),
    "price": row['price'].strip(),
    "install": row['install'].strip(),
    "tech_dept": row['tech'].strip(),
    "last_pm": row['lastpm'].strip(),
    "last_cm": row['lastcm'].strip(),
    "department": row['depart'].strip(),
    "site": row['site'].strip(),
    "div": row['div'].strip(),
    "ge_sys_no": row['ge'].strip()
}