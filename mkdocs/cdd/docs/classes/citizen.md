# Citizen Class

The `Citizen` model represents individuals with unique identification numbers and personal details.

## Fields

| Field Name     | Type          | Description                                                                 |
|----------------|---------------|-----------------------------------------------------------------------------|
| `numero_citoyen` | `CharField`  | A unique, auto-generated ID for the citizen. Not editable by users.         |
| `prenom`     | `CharField`  | The first name of the citizen.                                              |
| `middle_name`    | `CharField`  | The middle name of the citizen. Optional.                                   |
| `nom_de_famille`      | `CharField`  | The last name of the citizen.                                               |
| `date_de_naissance`  | `DateField`  | The citizen's date of birth.                                                |
| `sexe`         | `CharField`  | The gender of the citizen. Choices are: `Female` or `Male`.                |
| `numero_de_telephone`   | `CharField`  | The phone number of the citizen.                                            |
| `adresse`        | `CharField`  | The residential address of the citizen.                                     |

## Methods

### `__str__()`

Returns the full name of the citizen, including the middle name if present.

- **Example Output:**
  - `"John Doe"` if no middle name.
  - `"John Michael Doe"` if a middle name exists.

## Referenced in

The `Citizen` model is referenced in the following models:

- [RetireeProfile](retiree_profile.md)
- [TaxpayerProfile](taxpayer_profile.md)

## Applications

The `Citizen` model is used in the following applications:

- <a href="http://localhost:8030" target="_blank">CitizenAPI</a>
- <a href="http://localhost:8010" target="_blank">GovTax</a>
- <a href="http://localhost:8020" target="_blank">GovPension</a>