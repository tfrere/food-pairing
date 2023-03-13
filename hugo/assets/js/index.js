import $ from "jquery";
import autoComplete from "@tarekraafat/autocomplete.js";
import ingredientIndex from "../data/ingredient-index.json";

$results = $("#results");
$selection = $("#selection");
$meta = $("#meta");

const randomIntFromInterval = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1) + min);
};

const printResultItem = (item, url) => {
  $results.append(
    `<li class="results__item" data-slug="${item.slug}">
      <a class="results__item__link">

        <h5 class="results__item__link__number">${
          item.common_molecules.length
        }</h5>
        <h3 class="results__item__link__name">${item.name}</h3>

        <h5 class="results__item__link__cat">${item.category}</h5>
        <img class="results__item__link__image" src="${
          "ingredients/" + item.slug + "/images/preview.jpg"
        }"/>
      </a>
    </li>
    `
  );
};

const printSelectionItem = (data) => {
  $selection.append(
    `<li class="selection__item">
    <a class="results__item__link">
      <h2 class="selection__item__link__name">${data.name}</h2>
      <h5 class="results__item__link__cat">${data.category}</h5>
      <img class="selection__image" src="${
        "ingredients/" + data.slug + "/images/preview.jpg"
      }"/>      
    </a>
  </li>
  `
  );
};

const addResult = (slug) => {
  const url = "ingredients/" + slug;
  fetch(url + "/index.json")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      $selection.empty();
      printSelectionItem(data);

      $results.empty();
      data.ingredients_sharing_molecules.map((item) => {
        printResultItem(item, url);
      });
      $results.children().on("click", (item) => {
        console.log(item);
        addResult(item.currentTarget.dataset.slug);
      });
    });
};

window.addResult = addResult;

const randomIngredientIndex = randomIntFromInterval(0, ingredientIndex.length);

$meta.text(`${ingredientIndex.length}`);

console.log(randomIngredientIndex);
addResult(ingredientIndex[randomIngredientIndex].slug);

const autoCompleteJS = new autoComplete({
  selector: "#autoComplete",
  placeHolder: "Search for ingredients...",
  submit: true,

  data: {
    src: ingredientIndex,
    keys: ["name"],
    //cache: true,
  },
  resultItem: {
    highlight: true,
  },
});

autoCompleteJS.input.addEventListener("selection", function (event) {
  const feedback = event.detail;
  autoCompleteJS.input.blur();
  // Prepare User's Selected Value
  const selection = feedback.selection.value[feedback.selection.key];

  addResult(feedback.selection.value.slug);

  // Replace Input value with the selected value
  autoCompleteJS.input.value = selection;
  // Console log autoComplete data feedback
  console.log(feedback);
});
