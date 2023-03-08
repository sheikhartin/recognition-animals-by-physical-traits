## Recognition Animals by Physical Traits

![GitHub repo status](https://img.shields.io/badge/status-archived-yellowgreen?style=flat)
![GitHub license](https://img.shields.io/github/license/sheikhartin/recognition-animals-by-physical-traits)
![GitHub contributors](https://img.shields.io/github/contributors/sheikhartin/recognition-animals-by-physical-traits)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/sheikhartin/recognition-animals-by-physical-traits)
![GitHub repo size](https://img.shields.io/github/repo-size/sheikhartin/recognition-animals-by-physical-traits)

These days, animals traits are more important than ever for me, so I decided to create a simple app to help me recognize them more easily.

![A funny animal eating carrots](https://media.giphy.com/media/14uXQbPS73Y3qU/giphy.gif)

### Dataset

The original dataset provided by the [UCI machine learning repository](https://archive.ics.uci.edu/ml/datasets/zoo). The zoo dataset contains the following information:

- **Animal name**: Unique for each instance
- **Hair**: Boolean
- **Feathers**: Boolean
- **Eggs**: Boolean
- **Milk**: Boolean
- **Airborne**: Boolean
- **Aquatic**: Boolean
- **Predator**: Boolean
- **Toothed**: Boolean
- **Backbone**: Boolean
- **Breathes**: Boolean
- **Venomous**: Boolean
- **Fins**: Boolean
- **Legs**: Numeric (set of values between 0, 2, 4, 6 and 8)
- **Tail**: Boolean
- **Domestic**: Boolean
- **Catsize**: Boolean
- **Type**: Numeric (an integer in the range 1 to 7)

### Screenshots

![Page header that explains a bit about the project](screenshots/page-header-with-extended-sidebar.png)
![Display the dataset with selected features in tabular form](screenshots/dataset-table-section.png)
![When all models are applied, prints the "All done! 🎉" message](screenshots/all-models-applied.png)

### Usage

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

### License

This project is licensed under the MIT license found in the [LICENSE](LICENSE) file in the root directory of this repository.
