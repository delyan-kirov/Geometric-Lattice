G000001 := GraphByEdges([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]);
G000002 := GraphByEdges([[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [5, 3], [6, 1], [6, 4], [7, 2], [7, 4], [8, 3], [8, 4], [9, 5], [9, 6], [9, 7], [9, 8]]);
G000003 := GraphByEdges([[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 1], [6, 3], [7, 1], [7, 4], [8, 2], [8, 3], [8, 4], [9, 5], [9, 6], [9, 7], [9, 8]]);
G000004 := GraphByEdges([[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 1], [6, 3], [6, 4], [7, 2], [7, 3], [8, 2], [8, 4], [9, 5], [9, 6], [9, 7], [9, 8]]);
G000005 := GraphByEdges([[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [5, 4], [6, 1], [6, 3], [7, 2], [7, 3], [8, 3], [8, 4], [9, 5], [9, 6], [9, 7], [9, 8]]);
Lattices := [G000001, G000002, G000003, G000004, G000005];
LoadPackage("yags");

RemoveIsoImages := function(GraphList, GraphImage)
local len, i, element;
i := 0;
len := Length(GraphList);
for element in GraphList do
i := i + 1;
if IsIsomorphicGraph(element, GraphImage) then
Remove(GraphList, i);
fi;
od;
return GraphList;
end;

IsoFreeGraphs := [Lattices[1]];

for element in Lattices do
Lattices := RemoveIsoImages(Lattices, element);
Add(IsoFreeGraphs, Lattices[1]);
od;

GraphAutGps := [];
GraphAutSize := [];

for elements in Lattices do
Add(GraphAutGps, AutomorphismGroup(elements));
Add(GraphAutSize, Size(AutomorphismGroup(elements)));
od;

Print(GraphAutSize);
SaveWorkspace("workspace.g");
PrintTo("result.g", Length(Lattices));
quit;
