"""Exercise CLR generics, nested types, out parameters and value types."""

import acadsharp

def main() -> None:
    acadsharp.load()
    from ACadSharp import CadDocument
    from ACadSharp.Entities import Line, LwPolyline
    from CSMath import XYZ
    from System.Collections.Generic import List

    cad = CadDocument()
    line = Line(XYZ.Zero, XYZ(1, 2, 0))
    cad.Entities.Add(line)
    found, result = cad.TryGetCadObject[Line](line.Handle)
    assert found and result == line
    lines = List[Line]()
    lines.Add(line)
    assert lines.Count == 1
    point = line.StartPoint
    point.X = 10
    line.StartPoint = point
    assert line.StartPoint.X == 10
    vertex = LwPolyline.Vertex()
    assert vertex is not None
    assert acadsharp.get_type("ACadSharp.Entities.LwPolyline+Vertex") == LwPolyline.Vertex
    print("Verified generics, nested types, out parameters and struct reassignment")


if __name__ == "__main__":
    main()
