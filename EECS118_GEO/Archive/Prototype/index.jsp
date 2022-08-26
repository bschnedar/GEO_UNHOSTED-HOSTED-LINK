<%-- 
    Document   : index
    Created on : Nov 11, 2018, 12:26:37 PM
    Author     : Brandon schnedar
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ page import="java.util.*"%>
<%@ page import="java.io.*" %>


<!DOCTYPE html>
<html>
  <head>
    <title>Geometry Solver</title>   
  </head>
 

<body>
<p> Two triangles with 5 intersectining points </p>
  <b>Input Triangle One</b>
	<form method="post">
		TRIANGLE A
    	<input name="funcID" type="hidden" value="6">
		X <input name="x1a" type="number">
		Y  <input name="y1a" type="number">
		</br>
		X <input name="x2a" type="number">
		Y <input name="y2a" type="number"> 
		</br>
		X <input name="x3a" type="number">
		Y <input name="y3a" type="number"> 
		
		</br>
    	<input type="submit" value="Add">
	</form>
	
	 <b>Input Triangle Two</b>
	<form method="post">
		TRIANGLE B
    	<input name="funcID" type="hidden" value="6">
		X <input name="x1b" type="number">
		Y  <input name="y1b" type="number">
		</br>
		X <input name="x2b" type="number">
		Y <input name="y2b" type="number"> 
		</br>
		X <input name="x3b" type="number">
		Y <input name="y3b" type="number"> 
		
		</br>
    	<input type="submit" value="Add">
	</form>
	
  </br>  

  <img src="Diagram.jpg" alt="your disgram">
</body>
</html>




<% 
	double _x1a = request.getParameter("x1a");
	double _y1a = request.getParameter("y1a");
	double _x2a = request.getParameter("x2a");
	double _y2a = request.getParameter("y2a");
	double _x3a = request.getParameter("x3a");
	double _y3a = request.getParameter("y3a");
	
	double _x1b = request.getParameter("x1b");
	double _y1b = request.getParameter("y1b");
	double _x2b = request.getParameter("x2b");
	double _y2b = request.getParameter("y2b");
	double _x3b = request.getParameter("x3b");
	double _y3b = request.getParameter("y3b");
	
	
	//call python code here
%>
	</br>
	
	<p> <b>TRIANGLE A</b>
		POINT X:<%out.println(_x1a,_y1a);  %>
		POINT Y:<%out.println(_x2a,_y2a);  %>
		POINT Z:<%out.println(_x3a,_y3a);  %>
		
		Side 1: <%println("3.1622776601683795") %>
		Side 2: <%println("4.294182110716777") %>
		Side 3: <%println("3.104834939252005") %>
		
		Angle 1: <%println("46.193489423982044") %>
		Angle 2: <%println("47.31004222080242") %>
		Angle 3: <%A println("86.49646835521554") %>
		
		Area: <%println("4.9")%>
	</p>
	</br>
	<p> <b>TRIANGLE B</b>
		POINT X:<%out.println(_x1b,_y1b);  %>
		POINT Y:<%out.println(_x2b,_y2b);  %>
		POINT Z:<%out.println(_x3b,_y3b);  %>
		
		Side 1: <%println("2.8284271247461903") %>
		Side 2: <%println("3.605551275463989") %>
		Side 3: <%println("5.0") %>
		
		Angle 1: <%println("101.30993247402021") %>
		Angle 2: <%println("33.690067525979785") %>
		Angle 3: <%A println("45.0") %>
		
		Area: <%println("5.0")%>
			
	</p>
	</br>
	<p> <b>TWO TRIANGLES WITH FIVE INTERSECTIONS</b>
		<%

println("#TRIANGLE 1")
println("(1.4142135623730951, 1.8481160352690504, 0.9443110483358066, 30.06858282186243, 101.30993247402021, 48.62148470411735, 0.6547619047619048)")
println("#TRIANGLE 2")
println("(0.9480661802881197, 0.9287026012558761, 1.2567189039829543, 84.06847307508023, 47.31004222080242, 48.62148470411735, 0.43787878787878814)")
println("#TRIANGLE 3")
println("(1.7325376258723066, 1.0860200826829856, 1.9473684210526314, 84.06847307508023, 33.6900675259798, 62.24145939893999, 0.9357484620642508)")
println("#TRIANGLE 4")
println("(2.1081851067789197, 1.7192982456140353, 2.2600958477456725, 71.56505117707799, 46.19348942398205, 62.24145939893998, 1.719298245614035)")
println("#TRIANGLE 5")
println("(1.3333333333333333, 1.0540925533894598, 1.4142135623730951, 71.565051177078, 45.0, 63.43494882292201, 0.6666666666666667)")
println("big area")
println("2.742822966507177")

		%>
	</p>
  
  
  
 </br>
 


