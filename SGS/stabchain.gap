moregens := function(G, list) 
 local gens, i, Gs, orb, o; gens := []; for i in [1..Length(list)] do Gs := Stabilizer(G, list{[1..i-1]}, OnTuples); orb := Orbit(Gs, list[i]); for o in orb do AddSet(gens, RepresentativeAction(Gs, list[i], o)); od; od; return gens; end; 
PrintTo("new.g",moregens(SymmetricGroup(15),[1..15]));