{
  "targets": [{
    "target_name": "Notification",
    "sources": [ ],
    "conditions": [
      ['OS=="mac"', {
        "sources": [
          "Notification.cc",
          "mac_notification.mm",
          "notification_center_delegate.mm",
          "bundle_id_override.mm"
        ],
      }]
    ],
    "include_dirs": [
      "<!(node -e \"require('nan')\")"
    ],
    "xcode_settings": {
      "OTHER_CPLUSPLUSFLAGS": ["-std=c++17", "-stdlib=libc++", "-mmacosx-version-min=10.14"],
      "OTHER_LDFLAGS": ["-framework CoreFoundation -framework IOKit -framework AppKit"],
      "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
      "CLANG_CXX_LIBRARY": "libc++",
      "MACOSX_DEPLOYMENT_TARGET": "10.14"
    }
  }]
}