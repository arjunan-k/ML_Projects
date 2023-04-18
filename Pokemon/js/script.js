$(function () {
  var pokeapi = "https://pokeapi.co/api/v2/generation/1";
  var pokemonByName = "https://pokeapi.co/api/v2/pokemon/";

  $.getJSON(pokeapi)
  .done(function(data) {
    console.log(data);
    $.each(data.pokemon_species, function(index, pokemon) {
      var name = pokemon.name.charAt(0).toUpperCase() + pokemon.name.slice(1);
      var link = $('<a>').attr('id', pokemon.name).attr('href', `${pokemonByName}${pokemon.name}`).append($('<strong>').text(name))
      var paragraph = $("<p>").html("Pokemon species no. " + (index+1) + " is ").append(link);
      $('a').css({'color': '#0769ad', 'font-size': '22px', 'text-decoration': 'none', 'cursor': 'pointer'})

      link.click(function(event){
        event.preventDefault()
        $.getJSON(pokemonByName+pokemon.name)
        .done(function(details){
          console.log(details);
          var pokdiv = $('#pokemon-details');
          pokdiv.empty();
          pokdiv.append("<h2>" + name + "</h2>");
          pokdiv.append("<img src='" + details.sprites.front_default + "'>")
          pokdiv.append("<img src='" + details.sprites.back_default + "'>")
          pokdiv.append("<img src='" + details.sprites.front_shiny + "'>")
          pokdiv.append("<img src='" + details.sprites.back_shiny + "'>")
          $('img').css('width', '150px')

        })
        .fail()
        .always()
      })

      paragraph.appendTo("#pokedex");
    });
  })
  .fail(function() {
    console.log("Call to PokéAPI failed.");
  })
  .always(function() {
    console.log("Pokémon is awesome.")
  });
});