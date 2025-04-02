// Add an event listener to the "Calculate" button
document.getElementById("Calculate").addEventListener("click", function() {
    // Get the value from the "PPrice" input field, convert it to a float number
    const price = parseFloat(document.getElementById("PPrice").value);
    // Get the value from the "Litres" input field, convert it to a float number
    const litres = parseFloat(document.getElementById("Litres").value);
    // Calculate the total cost by multiplying price and litres
    const total = price * litres;
    // Update the content of the "totalamnt" element to display the total cost
    // The total is formatted to 2 decimal places and 'AED' is added to the result
    document.getElementById("totalamnt").textContent = total.toFixed(2) + 'AED';
});
