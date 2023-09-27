G000001 := GraphByEdges([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]);
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
