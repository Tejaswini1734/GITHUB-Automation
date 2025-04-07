// Source code is decompiled from a .class file using FernFlower decompiler.
package solutions;

import java.util.HashSet;
public class Solution {
   public Solution() {
   }

   public static boolean containsDuplicate(int[] var0) {
      HashSet var1 = new HashSet();
      int[] var2 = var0;
      int var3 = var0.length;

      for(int var4 = 0; var4 < var3; ++var4) {
         int var5 = var2[var4];
         if (var1.contains(var5)) {
            return true;
         }

         var1.add(var5);
      }

      return false;
   }
}
