import openvr
# https://github.com/cmbruns/pyopenvr


def main():
    # Should we look for VR input to detect AFK state or should
    # we just focus on getting the app title?
    #
    # Possibly useful endpoints:
    #   IVRApplications.getApplicationPropertyString
    #   IVRApplications.getApplicationPropertyString

    if openvr.isHmdPresent():
        print("VR head set found")

    if openvr.isRuntimeInstalled():
        print("Runtime is installed")

    vr_system = openvr.init(openvr.VRApplication_Utility)
    print(dir(vr_system))

    print(openvr.runtimePath())

    print(vr_system.getRecommendedRenderTargetSize())

    print(vr_system.isDisplayOnDesktop())

    def get_appkeys(ivrapps: openvr.IVRApplications):
        appkeys = []
        appcount = ivrapps.getApplicationCount()
        for idx in range(appcount):
            # TODO: I'm not sure how to handle buffer in this C++ interop context
            pchAppKeyBuffer = ''
            pchAppKeyBufferLen = 90
            error = ivrapps.getApplicationKeyByIndex(idx, pchAppKeyBuffer, pchAppKeyBufferLen)
            if error:
                print(error)
            appkeys.append(pchAppKeyBuffer)
        return appkeys

    def get_app(ivrapps: openvr.IVRApplications):
        for pchAppKey in get_appkeys(ivrapps):
            pchPropertyValueBuffer = ''
            unPropertyValueBufferLen = 90
            appname = ivrapps.getApplicationPropertyString(pchAppKey, openvr.VRApplicationProperty_Name_String, pchPropertyValueBuffer, unPropertyValueBufferLen)
            print(appname)



if __name__ == "__main__":
    main()
