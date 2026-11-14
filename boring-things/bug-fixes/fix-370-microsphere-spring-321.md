# Fix 370: microsphere-spring: the public test helper createPreFightRequest misspells pre-flight

Status: UNSENT and UNTESTED. Free to take.

- Project: microsphere-projects/microsphere-spring
- Bug report title: [Bug][test] Public API typo: createPreFightRequest should be createPreFlightRequest
- Bug report: number 321 ([open the bug report](https://github.com/microsphere-projects/microsphere-spring/issues/321))
- Project license: Apache-2.0
- Language: Java
- Test included: yes
- Patch file: [fixes/370-microsphere-spring-321.patch](fixes/370-microsphere-spring-321.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/370-microsphere-spring-321.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-370-microsphere-spring-321.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-370-microsphere-spring-321.html

## The bug

SpringTestWebUtils in the module microsphere-spring-test has a public method named createPreFightRequest. The documentation of the method says CORS pre-flight so the name is a misspelling that every user has to remember.

## The fix

The method is now named createPreFlightRequest. The old name stays as a deprecated method that calls the new one so existing callers keep working. A new test file checks both names.

## Files changed

- microsphere-spring-test/src/main/java/io/microsphere/spring/test/util/SpringTestWebUtils.java
- microsphere-spring-test/src/test/java/io/microsphere/spring/test/util/SpringTestWebUtilsPreFlightTest.java

## How to use the fix

1. Get a copy of the project microsphere-projects/microsphere-spring.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 370-microsphere-spring-321.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 321.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report offers a plain rename or a new method plus a deprecated old one for the case that releases exist. The fix keeps the old name because the chatbot could not tell whether a release already carries the method. Nobody compiled the change or ran the tests. Four test classes in the module microsphere-spring-web still call the old name and would show a deprecation warning. The report also mentions the header named :METHOD: and the fix leaves that header alone because the report proposes no change for it.

## Search words

microsphere-spring SpringTestWebUtils createPreFightRequest createPreFlightRequest CORS pre-flight deprecated rename

## The full patch

`````diff
diff --git a/microsphere-spring-test/src/main/java/io/microsphere/spring/test/util/SpringTestWebUtils.java b/microsphere-spring-test/src/main/java/io/microsphere/spring/test/util/SpringTestWebUtils.java
index b0c6762..f6a12ab 100644
--- a/microsphere-spring-test/src/main/java/io/microsphere/spring/test/util/SpringTestWebUtils.java
+++ b/microsphere-spring-test/src/main/java/io/microsphere/spring/test/util/SpringTestWebUtils.java
@@ -210,14 +210,14 @@ public abstract class SpringTestWebUtils {
      *
      * <h3>Example Usage</h3>
      * <pre>{@code
-     * NativeWebRequest preFlightRequest = SpringTestWebUtils.createPreFightRequest();
+     * NativeWebRequest preFlightRequest = SpringTestWebUtils.createPreFlightRequest();
      * }</pre>
      *
      * @return a new instance of {@link NativeWebRequest} configured for CORS pre-flight requests
      * @see #createWebRequest(Consumer)
      * @see MockHttpServletRequest
      */
-    public static NativeWebRequest createPreFightRequest() {
+    public static NativeWebRequest createPreFlightRequest() {
         // Create pre-flight request (OPTIONS method with Origin header)
         return createWebRequest(request -> {
             request.setMethod(OPTIONS.name());
@@ -227,6 +227,17 @@ public abstract class SpringTestWebUtils {
         });
     }
 
+    /**
+     * Creates a new instance of {@link NativeWebRequest} for CORS pre-flight requests.
+     *
+     * @return a new instance of {@link NativeWebRequest} configured for CORS pre-flight requests
+     * @deprecated the name is a misspelling, use {@link #createPreFlightRequest()} instead
+     */
+    @Deprecated
+    public static NativeWebRequest createPreFightRequest() {
+        return createPreFlightRequest();
+    }
+
     /**
      * Clears all attributes from the request scope of the given {@link NativeWebRequest}.
      * <p>
diff --git a/microsphere-spring-test/src/test/java/io/microsphere/spring/test/util/SpringTestWebUtilsPreFlightTest.java b/microsphere-spring-test/src/test/java/io/microsphere/spring/test/util/SpringTestWebUtilsPreFlightTest.java
new file mode 100644
index 0000000..a3b2237
--- /dev/null
+++ b/microsphere-spring-test/src/test/java/io/microsphere/spring/test/util/SpringTestWebUtilsPreFlightTest.java
@@ -0,0 +1,55 @@
+/*
+ * Licensed to the Apache Software Foundation (ASF) under one or more
+ * contributor license agreements.  See the NOTICE file distributed with
+ * this work for additional information regarding copyright ownership.
+ * The ASF licenses this file to You under the Apache License, Version 2.0
+ * (the "License"); you may not use this file except in compliance with
+ * the License.  You may obtain a copy of the License at
+ *
+ *     http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS,
+ * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+ * See the License for the specific language governing permissions and
+ * limitations under the License.
+ */
+
+package io.microsphere.spring.test.util;
+
+import org.junit.jupiter.api.Test;
+import org.springframework.mock.web.MockHttpServletRequest;
+import org.springframework.web.context.request.NativeWebRequest;
+
+import static io.microsphere.spring.test.util.SpringTestWebUtils.createPreFightRequest;
+import static io.microsphere.spring.test.util.SpringTestWebUtils.createPreFlightRequest;
+import static org.junit.jupiter.api.Assertions.assertEquals;
+import static org.springframework.http.HttpHeaders.ACCESS_CONTROL_REQUEST_METHOD;
+import static org.springframework.http.HttpHeaders.ORIGIN;
+
+/**
+ * {@link SpringTestWebUtils#createPreFlightRequest()} Test
+ *
+ * @see SpringTestWebUtils
+ * @since 1.0.0
+ */
+class SpringTestWebUtilsPreFlightTest {
+
+    @Test
+    void testCreatePreFlightRequest() {
+        assertPreFlightRequest(createPreFlightRequest());
+    }
+
+    @Test
+    @SuppressWarnings("deprecation")
+    void testDeprecatedNameStillWorks() {
+        assertPreFlightRequest(createPreFightRequest());
+    }
+
+    private void assertPreFlightRequest(NativeWebRequest webRequest) {
+        MockHttpServletRequest servletRequest = (MockHttpServletRequest) webRequest.getNativeRequest();
+        assertEquals("OPTIONS", servletRequest.getMethod());
+        assertEquals("*", servletRequest.getHeader(ORIGIN));
+        assertEquals("*", servletRequest.getHeader(ACCESS_CONTROL_REQUEST_METHOD));
+    }
+}
`````

[Back to the shelf](README.md)
