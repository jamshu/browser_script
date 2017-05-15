#! /bin/bash
echo "Select a Server:"
echo " * 1: Production"
echo " * 2: hiphone"
echo " * 3: Gsf"
echo " * 4: Ses"
echo " * 5: himatrix"
echo " * 6: Aroma"
echo " * 7: Development"
echo " * 8: Himatrix"
echo " * 9: Yas"
echo " * 91: Exit"


echo -n "Enter Your Choice >"
read SEL
case $SEL in
1)  
host=orchiderp.net
pass='Odoo#9447770001'
orchid_addons=orchid_addons
home=/opt/orchiderp
	echo "Select a Project:"
	echo " * 1: Beta Test"
	echo " * 2: Beta Live"
	echo " * 3: Asn Test"
	echo " * 4: Asn Live"
	echo " * 5: Rservice Test"
	echo " * 6: Rservice live"
	echo " * 7: Vibes Test"
	echo " * 8: Vibes live"
	echo " * 9: Office Test"
	echo " * 91: Office live"
	echo -n "Enter Your choice >"
	read choice
	case $choice in
		1) 
		project=beta_test
		instance=004-orchiderp-beta_test-server
		;;
		2)
		project=beta 
		instance=004-orchiderp-beta-server 
		;;
		3)
		project=asnTest8
		instance=004-orchiderp-asnTest8-server
		;;
		4)
		project=asnTest_orchid
		instance=004-orchiderp-asnTest_orchid-server
		;;
		5)
		project=r_services_test
		instance=004-orchiderp-r_services_test
		;;
		6)
		project=r_services_live
		instance=004-orchiderp-r_services_live
		;;
		7)
		project=vibes_test
		instance=004-orchiderp-vibes-test
		;;
		8)
		project=vibes
		instance=004-orchiderp-vibes-live
		;;
		9)
		project=office_test
		instance=004-orchiderp-office-test
		;;
		91)
		project=office
		instance=004-orchiderp-office-live
		;;
    esac
   ;;
2) 
host=128.199.247.125
pass='hpt@123'
home=/opt/hiphone
echo "Select a Project:"
	echo " * 1: Hiphone Test"
	echo " * 2: Hiphone Live"
	echo " * 5: Exit"
	echo -n "Enter Your choice >"
	read choice
	case $choice in
		1)
		project=test 
		instance=hiphone-test-server
        orchid_addons=orchid_addons
		;;
		2)
		project=live
		instance=hiphone-live-server
        orchid_addons=orchid_addons
		;; 
	esac
;;
3)
host=104.131.178.84
pass='Gsf#2015a1'
home=/opt/orchiderp
	echo "Select a Project:"
	echo " * 1: Gsf Test"
	echo " * 2: Gsf Live"
	echo " * 5: Exit"
	echo -n "Enter Your choice >"
	read choice
	case $choice in
		1)
		project=test 
		instance=orchiderp-test-server
        orchid_addons=orchid_addons
		;;
		2)
		project=live
		instance=orchiderp-live-server
        orchid_addons=orchid_addons
		;; 
	esac
;;
4)
host=104.236.215.84
pass='Ses#2015a1'
home=/opt/orchiderp
	echo "Select a Project:"
	echo " * 1: Ses Test"
	echo " * 2: Ses Live"
	echo " * 3: Exit"
	echo -n "Enter Your choice >"
	read choice
	case $choice in
		1)
		project=test 
		instance=orchiderp-test-server
        orchid_addons=orchiderp_addons
		;;
		2)
		project=live
		instance=orchiderp-live-server
        orchid_addons=orchiderp_addons
		;; 
	esac
;;
6)
host=128.199.199.28
pass='Del#2015a1'
home=/opt/delight/aroma
	echo "Select a Project:"
	echo " * 1: Aroma Test"
	echo " * 2: Aroma Live"
	echo " * 3: Exit"
	echo -n "Enter Your choice >"
	read choice
	case $choice in
		1)
		project=test 
		instance=001-orchid-aroma-test-server
        orchid_addons=orchid_addons
		;;
		2)
		project=live
		instance=001-orchid-aroma-live-server
        orchid_addons=orchid_addons
		;; 
	esac
;;

9)
host=128.199.148.185
pass='hggih;fv'
home=/opt/yas
	echo "Select a Project:"
	echo " * 1: Yas Test"
	echo " * 2: Yas Live"
	echo " * 3: Exit"
	echo -n "Enter Your choice >"
	read choice
	case $choice in
		1)
		project=test 
		instance=yastest-server
        orchid_addons=yas_addons
		;;
		2)
		project=live
		instance=yas-server
        orchid_addons=yas_addons
		;; 
	esac
;;


91) echo "Bye!"; exit ;;
*) echo "Please enter a valid option!"
esac
echo -n "Enter Module Name >"
read module 
loc=$home/$project/$orchid_addons/$module
echo $loc
echo Connecting to server......
sshpass -p $pass ssh -t admin@$host bash -c "'

   cd $loc
   sudo bzr pull
   sudo service $instance restart

'"



