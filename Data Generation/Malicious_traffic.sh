while true
do
	rndno="$(shuf -i 1-9 -n 1)"
	# printf "$rndno"
	# printf "\n"
	case "$rndno" in
	 	"1") hping3 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2
	 ;;
	 	"2") hping3 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2
	 ;;
	 	"3") hping3 -2 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2
	 ;;
	 	"4") hping3 -1 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2
	 ;;
	 	"5") hping3 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2
	 ;;
	 	"6") hping3 -1 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2
	 ;;
	 	"7") hping3 -2 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2
	 ;;
		 "8") hping3 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2
	 ;;
		 "9") hping3 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -2 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 200 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 600 10.0.0.2 &
			hping3 -1 --rand-source -i u10000 -c 2000 -d 1000 10.0.0.2
	 ;;
	esac
	
	sleep 21
done
