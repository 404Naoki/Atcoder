a = gets
list = a.chars.map(&:to_i)
puts list

i = 0

if list.uniq.size == 1
  puts "Weak"
elsif list.include?(9)
  while i < 3 do
    if list[i] == 9
      if list[i + 1] == 0
        if i == 2
          puts "Weak"
          break
        end
        i = i + 1
      else
        puts "Strong"
        break
      end
    else
      if list[i+1] == list[i] + 1
        if i == 2
          puts "Weak"
          break
        end
        i = i + 1
      else
        puts "Strong"
        break
      end
    end
  end

else
  while i < 3 do
    if list[i+1] == list[i] + 1
      if i == 2
        puts "Weak"
        break
      end
      i = i + 1
    else
      puts "Strong"
      break
    end
  end
end