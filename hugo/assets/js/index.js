import data from "../data/index.json";
import meta from "../data/meta.json";
import lunr from "lunr";
import $ from "jquery";

let $search = $("#search");
let $results = $("#results");
let $meta = $("#meta");
let $title = $("#title");
let $resultsLength = $("#results-length");

$meta.text(
  `Recipes : ${meta.total_recipes} | Ingredients : ${meta.total_ingredients}`
);

let searchLib = lunr(function () {
  let self = this;
  this.ref("id");
  self.field("title");
  self.field("tags");

  data.forEach((item) => {
    self.add(item);
  });
});

const randomIntFromInterval = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1) + min);
};

const printResultItem = (item) => {
  $results.append(
    `<li class="results__item">
      <a class="results__item__link" href="${
        document.location.origin
      }/recipes/${item.url}">
        <img class="results__item__link__image" src="${$("#" + item.url).attr(
          "src"
        )}"/>
        <h3 class="results__item__link__name">${item.name}</h3>
      </a>
    </li>
    `
  );
};

let randomIndexes = [];
for (let i = 0; i < 20; i++) {
  randomIndexes.push(randomIntFromInterval(0, data.length));
}

data.forEach((item, i) => {
  randomIndexes.forEach((index) => {
    if (index == i) {
      printResultItem(item);
    }
  });
});

$("#search").keyup(function () {
  let value = this.value.toLowerCase();
  let searchResult = searchLib.search(value);

  $title.text("search results");

  $results.empty();
  $resultsLength.text(searchResult.length);

  searchResult.map((item) => {
    printResultItem(data[parseInt(item.ref)]);
  });
});

// import elasticlunr from "elasticlunr";
// var index = elasticlunr(function () {
//   this.addField("title");
//   this.addField("tags");
//   this.addField("url");
//   this.addField("image_file_url");
//   this.setRef("id");
//   this.saveDocument(false);
// });

// data.forEach((item) => {
//   index.addDoc(item);
// });

// console.log(index.search("+tomato +aubergine"));
