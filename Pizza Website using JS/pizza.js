	
	/**********************************************************************************************
		This is the JS accompanying the pizza.html ordering page. It is a project to show ordering
		pizza using radio buttons/checkboexes to select ingredients and size, and to submit order as a form. 
		A receipt is returned to the screen, itemizing order and fees. 
		Final project of the JS course, Tech Academy. Laurie Roy, July-Aug 2017
		variables: selection, fee, running total are passed through each function
		
	***********************************************************************************************	
	 My thinking here is that I can have empty arrays, (that are reset by a cancel button (see clear below)).  
		The followig are arrays filled by the radio buttons. Need an order ID, and show receipt to customer. 
		(Then a submit order button.)  Customer selects a size, crust type, sauce, how much cheese
		and which ingredients they want on the pizza. (Eventually it'd be nice to add special instructions.) 
		These values are read in by a radio button the results are posted back to the page for the customer, 
		who either cancels the order or submits it (eventually).  */
	
	

	function getOrder()	{
		
		var selection = "Size: ";						// This initializes our string so it can get passed from  
		var fee = 0;													// function to function, growing line by line into a full receipt **might have to remove							
		var runningTotal = 0;											// numeric value, running total for all selected items. The above 3 globals are passed through.
// size selection
		var sizeTotal = 0;												// numeric value, subtotal of the selected pizza size
		var selectedSize = [];
		var form = document.getElementById("getSize"); 
		
		selectedSize.push(form.elements["getSize"].value);
		selection = selection+selectedSize+"<br>";					


			if (selectedSize[0] === "Personal Pizza") {				// reconcile the selected pizza size with its monetary value for our calculations
				sizeTotal = 6;
				} else if (selectedSize[0] === "Medium Pizza") {
					sizeTotal = 10;
				} else if (selectedSize[0] === "Large Pizza") {
					sizeTotal = 14;
				} else if (selectedSize[0] === "Extra Large Pizza") {
					sizeTotal = 16;
			} 
			runningTotal = sizeTotal;																			
			fee = fee+sizeTotal+"<br>";			
	
			getCrustType(runningTotal, selection, fee);								// give next command so enters into function
	};
// crust selection	
	function getCrustType(runningTotal,selection,fee)	{					// function to get crust type ordered, receives our running variables
		var crustTotal = 0;													// initialize variables						
		var selectedCrust = [];											
		var form = document.getElementById("crustType"); 
		
		selectedCrust.push(form.elements["crustType"].value);	
		selection = selection+"Crust choice: "+selectedCrust+"<br>";		 // *** I'm thinking I should be able to return to a div with each selection, not have to write the table.****
						 
			if (selectedCrust[0] === "Cheese Stuffed") {				// reconcile the selected pizza crust type with its monetary value for our calculations
				crustTotal = 3;					
			}
	
		runningTotal = runningTotal+crustTotal;	
		fee=fee+crustTotal+"<br>";
	
		getSauceType(runningTotal,selection,fee);								
	};

// sauce selection	 
	function getSauceType(runningTotal,selection,fee)	{					// function to get sauce type ordered, receives our running variables
		var sauceTotal = 0;												// initialize variables									
		var selectedSauce = [];											
		var sauceType = document.getElementById("sauceType");	
		var form = document.getElementById("sauceType"); 
		selectedSauce.push(form.elements["sauceType"].value);			
		selection = selection+"Sauce: "+selectedSauce+"<br>";
	
		//	if (selectedSauce === "") {				
				sauceTotal = 0;								// reconcile the selected pizza sauce type with its monetary value for our calculations
		//	} else {												// left in place in case want to charge for extra sauce or such
		//		sauceTotal = 0;
		//	} 
		runningTotal = runningTotal+sauceTotal;
		fee=fee+sauceTotal+"<br>";
		getCheeseType(runningTotal,selection,fee);								
	};

// cheese selection	 
	function getCheeseType(runningTotal,selection,fee)	{					// function to get Cheese type ordered, receives the running variables
		var cheeseTotal = 0;												// initialize variables										
		var selectedCheese = [];											
		var cheeseType = document.getElementsByName("cheeseType");	
		var form = document.getElementById("cheeseType"); 
		
		selectedCheese.push(form.elements["cheeseType"].value);			
		selection = selection+"Cheese: "+selectedCheese+"<br>";		
		
			if (selectedCheese[0] === "Extra cheese") {								// reconcile the selected pizza Cheese type with its monetary value for our calculations
				cheeseTotal = 3;
			} 
		runningTotal = runningTotal+cheeseTotal; 
		fee=fee+cheeseTotal+"<br>";
		getMeat(runningTotal,selection, fee);
	};

 // meat selection 

	 function getMeat(runningTotal,selection,fee) {									// using example from class tutorial passing in var
		var meatTotal = 0;															// initialize variables
		var selectedMeat = [];
		var meatArray = document.getElementById("toppings_meat");
		
		for (var j = 0; j < meatArray.length; j++) {								// iterate through choices for selection
			if (meatArray[j].checked) {
				selectedMeat.push(meatArray[j].value);
			}
	//		else {selection = selection+"Meats: none"+"<br>";
	//		}
		}
		var meats = selectedMeat.toString();										// display as string
		selection = selection+"Meats: "+meats+"<br>";
		var meatCount = selectedMeat.length;
		if (meatCount > 1) {
			meatTotal = (meatCount-1);												// account for the one free item. 
		}
		runningTotal = (runningTotal + meatTotal);
		fee= fee+meatTotal+"<br>";	
	
		getVeggies(runningTotal,selection,fee);
		}; 
// veggie selection
 		function getVeggies(runningTotal,selection,fee) {									// using example from class tutorial passing in var
			var veggieTotal = 0;															// initialize variables
			var selectedVeggies = [];
			var veggieArray = document.getElementById("toppings_veg");

			for (var j = 0; j < veggieArray.length; j++) {									// iterate through to get selected items
				if (veggieArray[j].checked) {
					selectedVeggies.push(veggieArray[j].value);
				}
			}
			/* else {selection = selection+"Veggies: none"+"<br>"; */
			var veggies = selectedVeggies.toString();
			selection = selection+"Veggies: "+veggies+"<br>"
			var veggieCount = selectedVeggies.length;
			if (veggieCount > 1) {
				veggieTotal = (veggieCount-1);										// account for the one free item
			}
			runningTotal = (runningTotal + veggieTotal);
			fee=fee+veggieTotal+"<br>";	
	
			document.getElementById("showText1").innerHTML=selection;
			document.getElementById("showText2").innerHTML=fee;
			document.getElementById("totalPrice2").innerHTML = "</h3>$"+runningTotal+".00"+"</h3>";
		};	
