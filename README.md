# Météo France

This package provides functionalities for interacting with the Meteo France API.

[Données climatologique de Météo France](https://portail-api.meteofrance.fr/web/fr/api/DonneesPubliquesClimatologie)

## Installation

You can install the package via `pip`:

```bash
pip install git+https://github.com/MalondaClement/meteo-france.git
```

## Usage

```python
# Import the package
from meteo_france import climatology

res = climatology.get_6m_stations_list(75, "your token")
```

## Contributing

Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests on [GitHub](https://github.com/MalondaClement/meteo-france).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MalondaClement/meteo-france/blob/main/LICENSE) file for details.
