# RetireeProfile Class

The `RetireeProfile` model represents retired citizens and their pension-related details.

## Fields

| Field Name               | Type             | Description                                                                                      |
|--------------------------|------------------|--------------------------------------------------------------------------------------------------|
| `citizen`                | `OneToOneField` | A one-to-one relationship with the [Citizen](citizen.md) model. Each retiree profile corresponds to one citizen. |
| `yearly_pension_allowance` | `DecimalField`  | The yearly pension allowance of the retiree, stored as a decimal value. Maximum: 10 digits with 2 decimal places. |

## Methods

### `__str__()`

Returns a string representation of the retiree profile, showing the associated citizen.

- **Example Output:**
  - `"Retiree Profile of John Doe"`

## Applications

The `RetireeProfile` model is used in the following applications:

- <a href="http://localhost:8020" target="_blank">GovPension</a>