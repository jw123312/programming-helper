# programming-helper for java

given:
```
private long Id;
private String name;
private String gender;
```




constructor() to generate a constructor which will return 
```
(long Id, String name, String gender) {
	this.Id = Id;
	this.name = name;
	this.gender = gender;
}
```

getsetmethod() will generate the get set methods
```
public long getId() {
	 return Id;
}

public void setId(long Id) {
	this.Id = Id;
}

public String getName() {
	 return name;
}

public void setName(String name) {
	this.name = name;
}

public String getGender() {
	 return gender;
}

public void setGender(String gender) {
	this.gender = gender;
}
```

tostringmethod() will generate the to string method
```
@Override
public String toString() {
	return "Id=" + Id + ", " +
		"Name=" + name + ", " +
		"Gender=" + gender;
}
```

