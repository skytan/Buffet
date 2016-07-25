#*********************************************************************
#
#   MODULE NAME:
#       file_copy - copy files
#
#   DESCRIPTION:
#       Copy files to the share folder
#
# Copyright 2015 by Garmin Ltd. or its subsidiaries.
#
#*********************************************************************

use strict;
use warnings;

=head
use GPM_lib;                                # Garmin Perl library
use GPM_prj_tbl;
use GPM_ini_utl;

GPM_lib::GPM_set_cwd();
GPM_lib::GPM_include_module( "GPM_login.pm" );
GPM_lib::GPM_include_module( "GPM_utl.pm"   );
=cut

my $target_prod = "Vivo_76xx";
my $DEFAULT_TARGET = "GPSMAP2208DS";
my $terminal_path = "\\\\c3-se-terminal3\\Shared_Folder\\Marine\\";
my $folder_path = "error";
my @dots;
my $path_file = "folder_path.ini";

if( ! -e "C:\\users\\".$ENV{'USERNAME'}."\\".$path_file )
    {
    #------------------------------------------------
    # Check your Shared_Folder path
    #------------------------------------------------
    opendir( DIR, $terminal_path ) || die "Can't open directory $terminal_path";
    @dots = readdir( DIR );
    foreach ( @dots )
        {
        if( index( $ENV{'USERNAME'}, lc( $_ ) ) != -1 )
            {
            $folder_path = $terminal_path.$_;
            last;
            }
        }
    closedir DIR;

    if( $folder_path eq "error" )
        {
        die "Plese check whether you have the permission of $terminal_path!!!\n";
        }
    #------------------------------------------------
    # Write path to the file
    #------------------------------------------------
    open( PATH_FILE, ">C:\\users\\".$ENV{'USERNAME'}."\\".$path_file ) or die("Create file error!\n");
    print PATH_FILE $folder_path;
    close PATH_FILE;
    }
else
    {
    open( PATH_FILE, "<C:\\users\\".$ENV{'USERNAME'}."\\".$path_file ) or die("Reading file Error!\n");
    $folder_path = <PATH_FILE>;
    close PATH_FILE;
    }

#$target_prod = GPM_ini_utl::GPM_read_ini_val( $GPM_prj_tbl::INI_FNAME, $GPM_prj_tbl::TARGET_PROD_KEY, $DEFAULT_TARGET );

#------------------------------------------------
# Check folders if valid
#------------------------------------------------
if( ! -e $folder_path."\\Echomap\\".$target_prod )
    {
    system( "mkdir ".$folder_path."\\Echomap\\".$target_prod."\\bin" );
    system( "mkdir ".$folder_path."\\Echomap\\".$target_prod."\\simulator\\res\\" );
    }

my $start_time = time();

#------------------------------------------------
# Temp file
#------------------------------------------------
my $target = "C:\\users\\".$ENV{'USERNAME'}."\\temp.zip";
my $source;

#------------------------------------------------
# Copy files according to the commands
#------------------------------------------------
if( $ARGV[0] eq "SIM" )
	{
	$source = "\.\\build\\76xx-v-win\\debug\\sys.exe";

	print "Copying sim_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
	system( "\"C:\\Program Files\\7-Zip\\7z\" a -y ".$target." ".$source."" );
	system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\simulator\\ws-".$target_prod.".zip" );
	
	unlink( $target );
	}
elsif( $ARGV[0] eq "REC" )
	{
	$source = "\.\\build\\76xx-v-win\\debug\\resources\\";

	print "Copying sys_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
	system( "\"C:\\Program Files\\7-Zip\\7z\" a -y ".$target." ".$source."" );
	system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\simulator\\res\\res-".$target_prod.".zip" );
	
	unlink( $target );
	}
elsif( $ARGV[0] eq "SYS" )
    {
	$source = "\.\\build\\76xx-v\\release\\sys.bin";
	
    print "Copying sys_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
    system( "\"C:\\Program Files\\7-Zip\\7z\" a -y ".$target." ".$source."" );
    system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\bin\\SYS_".$target_prod.".zip" );

    unlink( $target );
    }
elsif( $ARGV[0] eq "LDR" )
    {
	$target = "\.\\build\\76xx-v\\release\\ldr.bin";
	
    print "Copying ldr_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
    system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\bin" );
    }
elsif( $ARGV[0] eq "BB" )
    {
	$target = "\.\\build\\76xx-v\\release\\bb.bin";
	
    print "Copying bb_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
    system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\bin" );
    }
else
    {
    die "NO such command at this point.\n";
    }
	
=head
#------------------------------------------------
# Copy files according to the commands
#------------------------------------------------
if( $ARGV[0] eq "SYS" )
    {
    print "Copying sys_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
    system( "\"C:\\Program Files\\7-Zip\\7z\" a -y ".$target." SYS_".$target_prod.".bin " );
    system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\bin\\SYS_".$target_prod.".zip" );

    unlink( $target );
    }
elsif( $ARGV[0] eq "BB" )
    {
    print "Copying bb_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
    system( "Copy bb_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin" );
    }
elsif( $ARGV[0] eq "LDR" )
    {
    print "Copying ldr_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin";
    system( "Copy ldr_".$target_prod.".bin ".$folder_path."\\Echomap\\".$target_prod."\\bin" );
    }
elsif( $ARGV[0] eq "SIM" )
    {
    my $postfix;
    if( $target_prod eq "SVGA-80" )
        {
        $postfix = "echoMAP_80";
        }
    else
        {
        $postfix = $target_prod;
        }
    print "Copy ws-".$postfix.".exe ".$folder_path."\\Echomap\\".$target_prod."\\simulator";
    system( "\"C:\\Program Files\\7-Zip\\7z\" a -y ".$target." ws-".$postfix.".exe " );
    system( "Copy ".$target." ".$folder_path."\\Echomap\\".$target_prod."\\simulator\\ws-".$postfix.".zip" );

    unlink( $target );
    }
else
    {
    die "NO such command at this point.\n";
    }
=cut

my $end_time = time();
print "Copy Completed in ",$end_time-$start_time," Seconds\n";
