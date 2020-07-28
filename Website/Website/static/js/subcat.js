 function dynamicdropdown(listindex)
            {
                document.getElementById("subcategory").length = 0;
                switch (listindex)
                {
                    case "1" :
                        document.getElementById("subcategory").options[0]=new Option("Select Car type","");
                        document.getElementById("subcategory").options[1]=new Option("Cars ","");
                        document.getElementById("subcategory").options[2]=new Option("Spare Parts ","");
                        break;

                    case "2" :
                        document.getElementById("subcategory").options[0]=new Option("Select Furniture type","");
                        document.getElementById("subcategory").options[1]=new Option("Sofa & Dining ","");
                        document.getElementById("subcategory").options[2]=new Option("Beds & Wardrobes","");
                        break;
                    case "3" :
                        document.getElementById("subcategory").options[0]=new Option("Select Electronics & Appliances type","");
                        document.getElementById("subcategory").options[1]=new Option("Kitchen & Other Appliances","");
                        document.getElementById("subcategory").options[2]=new Option("Computers & Laptops","");
                        document.getElementById("subcategory").options[3]=new Option("Fridges","");
                        document.getElementById("subcategory").options[4]=new Option("Hard Disks, Printers & Monitors","");
                        document.getElementById("subcategory").options[5]=new Option("Washing Machines","");
                        break;
                    case "4" :
                        document.getElementById("subcategory").options[0]=new Option("Select Mobile type","");
                        document.getElementById("subcategory").options[1]=new Option("Mobile Phones","");
                        document.getElementById("subcategory").options[1]=new Option("Accessories ","");
                        break;
                }
                return true;
            }