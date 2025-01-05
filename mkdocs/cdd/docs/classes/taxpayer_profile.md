# TaxpayerProfile Class

The `TaxpayerProfile` model extends the [Citizen](citizen.md) model by providing tax-related details.

## Fields

| Field Name            | Type             | Description                                                                                     |
|-----------------------|------------------|-------------------------------------------------------------------------------------------------|
| `citizen`             | `OneToOneField` | A one-to-one relationship with the [Citizen](citizen.md) model. Each taxpayer profile corresponds to one citizen. |
| `total_tax_contribution` | `DecimalField`  | The total tax contribution of the citizen, stored as a decimal value. Maximum: 10 digits with 2 decimal places. |

## Methods

### `__str__()`

Returns a string representation of the taxpayer profile, showing the associated citizen.

- **Example Output:**
  - `"Taxpayer Profile of John Doe"`

## Applications

The `TaxpayerProfile` model is used in the following applications:

- <a href="http://localhost:8010" target="_blank">GovTax</a>
- <a href="http://localhost:8020" target="_blank">GovPension</a>