import matplotlib.pyplot as plt
import numpy as np


def genereaza_date_simulate(numar_zile, temp_medie, temp_dev_std, precip_medie, precip_dev_std, corelatie):
    # Generăm temperaturi simulate
    temperaturi_simulate = np.random.normal(temp_medie, temp_dev_std, numar_zile)

    # Ajustăm media precipitațiilor bazată pe temperatura simulată
    precip_medie_ajustata = precip_medie - corelatie * (temperaturi_simulate - temp_medie)

    # Generăm precipitații simulate cu media ajustată
    precipitatii_simulate = np.random.normal(precip_medie_ajustata, precip_dev_std, numar_zile)

    # Asigurăm că precipitațiile nu sunt negative
    precipitatii_simulate = np.where(precipitatii_simulate < 0, 0, precipitatii_simulate)

    return temperaturi_simulate, precipitatii_simulate


# Parametrii de bază
nr_zile_1 = 365
temp_medie_1 = 20  # Temperatura medie istorică (în grade Celsius)
temp_dev_std_1 = 5  # Deviația standard a temperaturii
precip_medie_1 = 2  # Media precipitațiilor zilnice (în mm)
precip_dev_std_1 = 1.5  # Deviația standard a precipitațiilor
corelatie_1 = 0.1  # Factorul de corelație între temperatură și precipitații

# Generăm date simulate
temperaturi, precipitatii = genereaza_date_simulate(nr_zile_1,
                                                    temp_medie_1,
                                                    temp_dev_std_1,
                                                    precip_medie_1,
                                                    precip_dev_std_1,
                                                    corelatie_1)

# Vizualizăm rezultatele
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(temperaturi, precipitatii, alpha=0.5)
plt.title("Corelația între Temperatură și Precipitații")
plt.xlabel("Temperatură (°C)")
plt.ylabel("Precipitații (mm)")

plt.subplot(1, 2, 2)
plt.hist(temperaturi, bins=30, color='blue', alpha=0.7, label="Temperatură")
plt.hist(precipitatii, bins=30, color='green', alpha=0.7, label="Precipitații")
plt.title("Distribuții de Temperatură și Precipitații")
plt.xlabel("Valori")
plt.ylabel("Frecvență")
plt.legend()

plt.tight_layout()
plt.show()
