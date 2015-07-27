{##########################################}
{#           Nikola Radmanovic            #}
{#      http://www.github.com/Radmanovic  #}
{#                2015                    #}
{##########################################}
Program Prosek(output);
{Variable's}
var a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, s, P:Real;
var ime, prezime: String;
begin
  {Informacije}
  writeln('Unesite ime i prezime ucenika:');
  readln(ime, prezime);
  {Predmeti}
  writeln('Unesite vasu ocenu iz maternjeg jezika');
  readln(a);
  
  writeln('Unesite ocenu iz I stranog jezika');
  readln(b);
  
  writeln('Unesite vasu ocenu iz II stranog jezika');
  readln(c);
  
  writeln('Unesite vasu ocenu iz fizike');
  readln(d);
  
  writeln('Unesite vasu ocenu iz geografije');
  readln(e);
  
  writeln('Unesite vasu ocenu iz hemije');
  readln(f);
  
  writeln('Unesite vasu ocenu iz biologije');
  readln(g);
  
  writeln('Unesite vasu ocenu iz matematike');
  readln(h);
  
  writeln('Unesite vasu ocenu iz istorije');
  readln(i);
  
  writeln('Unesite vasu ocenu iz latinskog jezika');
  readln(j);
  
  writeln('Unesite vasu ocenu iz psihologije');
  readln(k);
  
  writeln('Unesite vasu ocenu iz likovne kulture');
  readln(l);
  
  writeln('Unesite vasu ocenu iz muziicke kulture');
  readln(m);
  
  writeln('Unesite vasu ocenu iz fizickog vaspitanja');
  readln(n);
  
  writeln('Unesite vasu ocenu iz vladanja');
  readln(o);
      
  s:=(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o); {Sabira sve ocena}
  P:=s/15; {Vrsi sracunavanje aritmeticke vrednosti}
  {Kraj}
  write('Ime ucenika: ',ime,' ',prezime);
  read;
  writeln('Prosek: ',P); {Ispisuje aritmeticku vrednost}
  readln;
  write('Trenutno koristite verziju 0.0.1'); 
  write('Hvala sto ste koristili program source code se nalazi na http://www.github.com/Radmanovic/Prosek');
end.
