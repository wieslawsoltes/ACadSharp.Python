#ifndef ACADSHARP_NATIVE_H
#define ACADSHARP_NATIVE_H

#ifdef __cplusplus
extern "C" {
#endif

/* ABI 1. The library embeds .NET NativeAOT; no installed CLR is required.
 * Requests and responses are null-terminated UTF-8 JSON strings.
 * Each non-null response belongs to the caller, including error responses,
 * and MUST be released exactly once using acadsharp_free (not libc free).
 * Calls are serialized internally. Object handles are process-local integers.
 * Releasing a handle removes the bridge reference; it does not call Dispose.
 * No managed exception is intentionally allowed to cross this C boundary.
 */
int acadsharp_abi_version(void);
char *acadsharp_call(const char *request);
void acadsharp_free(char *response);

#ifdef __cplusplus
}
#endif
#endif
