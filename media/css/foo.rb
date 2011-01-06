
(0..19).each do |row| 
  (0..24).each do |col| 
    puts ".p_img_#{row}_#{col} { " +
         "background: url('/static/img/pokemon_sprites.png') no-repeat " +
         "scroll #{-col*80}px #{-row*80}px transparent; }"
       
  end
end
