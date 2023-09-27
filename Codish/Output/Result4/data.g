G000001 := GraphByEdges([[1, 0], [2, 0], [3, 1], [3, 2]]);
Lattices := [G000001];
LoadPackage("yags");
IsoFreeGraphs := [];

while Length(Lattices) > 0 do 
  Add(IsoFreeGraphs, Lattices[1]);
  Lattices := Filtered(Lattices, x -> not IsIsomorphicGraph(x, Lattices[1]));
od;

GraphAutGps := [];
GraphAutSize := [];

for elements in IsoFreeGraphs do
Add(GraphAutGps, AutomorphismGroup(elements));
Add(GraphAutSize, Size(AutomorphismGroup(elements)));
od;

Print("Graph group sizes: ");
Print(GraphAutSize);
SaveWorkspace("workspace.g");
PrintTo("result.g", Length(IsoFreeGraphs));
quit;
