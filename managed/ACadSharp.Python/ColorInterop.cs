namespace ACadSharp.Python;

/// <summary>
/// Copies upstream stack-only color spans into arrays that Python.NET can marshal.
/// </summary>
/// <remarks>
/// These methods call the original upstream operations. Palette lookup, true-color
/// handling, sentinels and exception behavior are implemented only by ACadSharp.
/// </remarks>
public static class ColorInterop
{
    /// <summary>Return a copy of the RGB bytes returned by Color.GetRgb.</summary>
    public static byte[] GetRgb(Color color) => color.GetRgb().ToArray();

    /// <summary>Return a copy of the RGB bytes returned by Color.GetTrueColorRgb.</summary>
    public static byte[] GetTrueColorRgb(Color color) => color.GetTrueColorRgb().ToArray();

    /// <summary>Return a copy of the RGB bytes returned by Color.GetIndexRGB.</summary>
    public static byte[] GetIndexRGB(byte index) => Color.GetIndexRGB(index).ToArray();
}
