{##########################################}
{#           Nikola Radmanovic            #}
{#      http://www.github.com/Radmanovic  #}
{#                2015                    #}
{##########################################}
Program Prosek(output);
  {Variable's}
  var a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, s, izb, P:Real;
  var ime, prezime, drzava, opstina, mesto, skola:String;

begin
  {Informacije}
  writeln('Unesite drzavu opstinu i mesto:');
  readln(drzava, opstina, mesto);
  
  writeln('Unesite ime skole:');
  readln(skola);
  
  writeln('Unesite ime i prezime ucenika:');
  readln(ime, prezime);
  {Predmeti}
  writeln('Unesite ocenu iz maternjeg jezika');
  readln(a);
  
  writeln('Unesite ocenu iz I stranog jezika');
  readln(b);
  
  writeln('Unesite ocenu iz II stranog jezika');
  readln(c);
  
  writeln('Unesite ocenu iz fizike');
  readln(d);
  
  writeln('Unesite ocenu iz geografije');
  readln(e);
  
  writeln('Unesite ocenu iz hemije');
  readln(f);
  
  writeln('Unesite ocenu iz biologije');
  readln(g);
  
  writeln('Unesite ocenu iz matematike');
  readln(h);
  
  writeln('Unesite ocenu iz istorije');
  readln(i);
  
  writeln('Unesite ocenu iz latinskog jezika');
  readln(j);
  
  writeln('Unesite ocenu iz psihologije');
  readln(k);
  
  writeln('Unesite ocenu iz likovne kulture');
  readln(l);
  
  writeln('Unesite ocenu iz muziicke kulture');
  readln(m);
  
  writeln('Unesite ocenu iz fizickog vaspitanja');
  readln(n);
  
  writeln('Unesite ocenu iz verske nastave/gradjanskog vaspitanja');
  readln(izb); 
  
  writeln('Unesite ocenu iz vladanja');
  readln(o);
  
  {Matematicke operacije}  
  s:=(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o); {Sabira sve ocena}
  P:=s/15; {Vrsi sracunavanje aritmeticke vrednosti}
  
  {Kraj}
  write('Informacije: ',drzava,' ',opstina);
  read;
  writeln(' ',mesto,' ',skola);
  readln; 
  
  write('Ime ucenika: ',ime,' ',prezime);
  read;
  writeln('Prosek: ',P); {Ispisuje aritmeticku vrednost}
  readln;
  {Credits & Version}
  write('Trenutno koristite verziju 0.0.1'); 
  readln;
  write('Hvala sto ste koristili program source code se nalazi na http://www.github.com/Radmanovic/Prosek');
end.
