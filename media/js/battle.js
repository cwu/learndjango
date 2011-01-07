function makeMove(move_num)
{
  $.ajax({  url: battle_move_url,
            type: 'POST',
            dataType: 'json',
            data: {
              battle_id: battle_id,
              move: move_num,
            },
            success: function(data) { 
              if (!data || !data.success)
                return;

              data = data.data;
              $("#player_hp_left").text(data.poke1.hp_left);
              $("#opponent_hp_left").text(data.poke2.hp_left);
              $("#move1").text(data.move1);
              $("#move2").text(data.move2);
              $("#battle_history").text($("#battle_history").text() + data.battle_lines);
            },
            error: function(xhr, msg, err) { 
              response = JSON.parse(xhr.responseText);
              alert(msg + "|" + response.errors.msg);
            }
         });
}

var battle_id; 
var battle_move_url; 
$("#battle_container").ready(function() {
  battle_id = $("#battle_container").attr("battle_id");
  battle_move_url = $("#battle_container").attr("battle_move_url"); 
});

$("#move1").live("click", function() { makeMove('1'); });
$("#move2").live("click", function() { makeMove('2'); });
