

def create_batch_submission_script(cmssw_cfg_file):
    outname = cmssw_cfg_file.split(".py")[0] + ".sh"
    print "Submission script name: " + outname
    
    out_file = open(outname, "w")

    out_file.write("#!/bin/bash\n\n")
    out_file.write("cmsRun " + cmssw_cfg_file + "\n")

    out_file.close()


create_batch_submission_script("bla_cfg.py")
