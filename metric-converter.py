
import re

def SIUnitsConversion(units):
	
	units = units.strip();
	
	#convert volume to SI units (i.e. meters)
	if "in" in units or "inch" in units or "\"" in units or "''" in units or "``" in units:
		factor = 0.0254;		
	elif "ft" in units or "foot" in units or "feet" in units or "'" in units or "`" in units:
		factor = 0.3048;
	elif "yard" in units:
		factor = 0.9144;
	else:
		factor = 1;
	
	#convert weight to SI units (i.e. grams)
	if "oz" in units or "ounce" in units:
		factor = 28.3495;		
	elif "lb" in units or "pound" in units:
		factor = 453.592;
	elif "ton" in units:
		factor = 10**6;
	elif factor is None:
		factor = 1;
	
	#scale units according to SI prefix
	if "kilo" in units or re.search(r"(?<=k)(g|m|s|K|A|cd|mol)\b", units):
		scale = 10**3;
	elif "Mega" in units or re.search(r"(?<=M)(g|m|s|K|A|cd|mol)\b", units):
		scale = 10**6;	
	elif "deci" in units or re.search(r"(?<=d)(g|m|s|K|A|cd|mol)\b", units):
		scale = 10**-1;	
	elif "centi" in units or re.search(r"(?<=c)(g|m|s|K|A|cd|mol)\b", units):
		scale = 10**-2;	
	elif "milli" in units or re.search(r"(?<=m)(g|m|s|K|A|cd|mol)\b", units):
		scale = 10**-3;		
	elif "micro" in units or re.search(r"(?<=\u03BC)(g|m|s|K|A|cd|mol)\b", units):
		scale = 10**-6; print("scaling")
	else:
		scale = 1;
	
	#print({"scale": scale, "factor": factor});
	return {"scale": scale, "factor": factor};

def convertUnits(inputStr, inputUnits, outputUnits):
	
	inputStr = str(inputStr);	#Ensure input is a string
	data = re.search("([\d\.]+)\s*(\w+)*", inputStr);
	
	try:
		inputValue = float(data.group(1));
	except AttributeError:
		print("'{}' is an invalid input. Please enter a numeric value".format(inputStr))
		return;	
	
	if not inputUnits or not isinstance(inputUnits, str):
		print("Please enter an input unit as string");
		return;
		
	if not outputUnits or not isinstance(outputUnits, str):
		print("Please enter an output unit as string")
		return;
		
	inputSI = SIUnitsConversion(inputUnits);
	outputSI = SIUnitsConversion(outputUnits);
	
	convertedValue = inputValue * inputSI["scale"] * inputSI["factor"] / outputSI["scale"] / outputSI["factor"];
	#print("{} {} = {} {}".format(inputValue, inputUnits, convertedValue, outputUnits));
	return convertedValue;

def main():
	inputStr = "1";
	inputUnits = "kilometer"
	outputUnits = "inch";	
	convertUnits(inputStr, inputUnits, outputUnits);
	
if __name__ == '__main__':	
	main();