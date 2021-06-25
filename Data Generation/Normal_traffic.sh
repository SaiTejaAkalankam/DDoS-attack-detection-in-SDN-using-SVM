while true
do
	rndip="$(shuf -i 2-4 -n 1)"
	rndtraffictypenumber="$(shuf -i 1-3 -n 1)"
	rndpacketsize="$(shuf -i 100-1500 -n 1)"
	rndpps="$(shuf -i 10-1000 -n 1)"
	rndduration="$(shuf -i 3000-4000 -n 1)"
	if [ $rndtraffictypenumber -eq 1 ]; then
		rndtraffictype="TCP"
	elif [ $rndtraffictypenumber -eq 2 ]; then
		rndtraffictype="UDP"
	else
		rndtraffictype="ICMP"
	fi
	
	ITGSend -T $rndtraffictype -a 10.0.0.1 -c $rndpacketsize -C $rndpps -t $rndduration &
	ITGSend -T $rndtraffictype -a 10.0.0.2 -c $rndpacketsize -C $rndpps -t $rndduration &
	ITGSend -T $rndtraffictype -a 10.0.0.3 -c $rndpacketsize -C $rndpps -t $rndduration &
	ITGSend -T $rndtraffictype -a 10.0.0.4 -c $rndpacketsize -C $rndpps -t $rndduration &
	ITGSend -T $rndtraffictype -a 10.0.0.5 -c $rndpacketsize -C $rndpps -t $rndduration &
	ITGSend -T $rndtraffictype -a 10.0.0.6 -c $rndpacketsize -C $rndpps -t $rndduration &
	ITGSend -T $rndtraffictype -a 10.0.0.7 -c $rndpacketsize -C $rndpps -t $rndduration
	
	sleep $((($rndduration / 1000) + 2))
done
